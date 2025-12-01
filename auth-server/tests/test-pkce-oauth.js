const crypto = require('crypto');

// Test credentials
const TEST_EMAIL = 'admin@robolearn.io';
const TEST_PASSWORD = 'Admin123!';

// Generate PKCE verifier and challenge
function generateCodeVerifier() {
  const array = crypto.randomBytes(32);
  return array.toString('base64url');
}

function generateCodeChallenge(verifier) {
  const hash = crypto.createHash('sha256').update(verifier).digest();
  return hash.toString('base64url');
}

async function testPKCEFlow() {
  console.log('=== Testing PKCE OAuth Flow ===\n');

  // Step 1: Generate PKCE values
  const codeVerifier = generateCodeVerifier();
  const codeChallenge = generateCodeChallenge(codeVerifier);
  console.log('1. Generated PKCE values:');
  console.log('   Code Verifier: ' + codeVerifier.slice(0, 20) + '...');
  console.log('   Code Challenge: ' + codeChallenge.slice(0, 20) + '...\n');

  // Step 2: Sign in to get session cookie
  console.log('2. Signing in to get session...');
  const signInResponse = await fetch('http://localhost:3001/api/auth/sign-in/email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: TEST_EMAIL, password: TEST_PASSWORD }),
  });

  const cookies = signInResponse.headers.get('set-cookie');
  console.log('   Sign-in status: ' + signInResponse.status);
  console.log('   Session cookie received: ' + (cookies ? 'YES' : 'NO') + '\n');

  if (!signInResponse.ok) {
    const err = await signInResponse.text();
    console.log('   Error:', err);
    return;
  }

  // Step 3: Request authorization with PKCE
  const authUrl = 'http://localhost:3001/api/auth/oauth2/authorize?client_id=robolearn-public-client&redirect_uri=' +
    encodeURIComponent('http://localhost:3000/auth/callback') +
    '&response_type=code&scope=openid%20profile%20email&state=test&code_challenge=' +
    codeChallenge + '&code_challenge_method=S256';

  console.log('3. Requesting authorization code with PKCE...');
  const authResponse = await fetch(authUrl, {
    headers: { Cookie: cookies },
    redirect: 'manual',
  });

  console.log('   Auth status: ' + authResponse.status);
  
  // Better Auth returns JSON with redirect info instead of HTTP redirect
  let code;
  if (authResponse.status === 200) {
    const authBody = await authResponse.json();
    if (authBody.redirect && authBody.url) {
      const codeMatch = authBody.url.match(/code=([^&]+)/);
      if (codeMatch) {
        code = codeMatch[1];
        console.log('   Redirect URL: ' + authBody.url.slice(0, 60) + '...');
      }
    }
  } else if (authResponse.status === 302) {
    const location = authResponse.headers.get('location');
    const codeMatch = location?.match(/code=([^&]+)/);
    if (codeMatch) {
      code = codeMatch[1];
    }
  }

  if (!code) {
    const body = await authResponse.text();
    console.log('   No code received. Response:', body);
    return;
  }
  
  console.log('   Got authorization code: ' + code.slice(0, 20) + '...\n');

  // Step 4: Exchange code for tokens WITH PKCE (no client_secret!)
  console.log('4. Exchanging code for tokens (using PKCE, no secret)...');
  const tokenResponse = await fetch('http://localhost:3001/api/auth/oauth2/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      code,
      redirect_uri: 'http://localhost:3000/auth/callback',
      client_id: 'robolearn-public-client',
      code_verifier: codeVerifier,  // PKCE: verifier instead of secret
    }),
  });

  console.log('   Token exchange status: ' + tokenResponse.status);

  if (tokenResponse.ok) {
    const tokens = await tokenResponse.json();
    console.log('   Access token: ' + (tokens.access_token ? 'YES' : 'NO'));
    console.log('   Refresh token: ' + (tokens.refresh_token ? 'YES' : 'NO'));
    console.log('   ID token: ' + (tokens.id_token ? 'YES' : 'NO'));
    console.log('   Token type: ' + tokens.token_type);
    console.log('   Expires in: ' + tokens.expires_in + 's\n');

    // Step 5: Get userinfo
    console.log('5. Fetching userinfo...');
    const userinfoResponse = await fetch('http://localhost:3001/api/auth/oauth2/userinfo', {
      headers: { Authorization: 'Bearer ' + tokens.access_token },
    });

    if (userinfoResponse.ok) {
      const userinfo = await userinfoResponse.json();
      console.log('   Userinfo:', JSON.stringify(userinfo, null, 2));
      console.log('\n=== PKCE OAuth Flow: SUCCESS ===');
    } else {
      console.log('   Userinfo error: ' + userinfoResponse.status);
      console.log('   Error:', await userinfoResponse.text());
    }
  } else {
    const err = await tokenResponse.text();
    console.log('   Token exchange failed:', err);
    console.log('\n=== PKCE OAuth Flow: FAILED ===');
  }
}

testPKCEFlow().catch(console.error);
