import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import { pgTable, text, boolean } from "drizzle-orm/pg-core";
import { eq } from "drizzle-orm";
import dotenv from "dotenv";

dotenv.config({ path: ".env.local" });

const user = pgTable("user", {
  id: text("id").primaryKey(),
  email: text("email").notNull().unique(),
  emailVerified: boolean("email_verified").default(false).notNull(),
});

const sql = neon(process.env.DATABASE_URL!);
const db = drizzle(sql);

async function main() {
  const result = await db.update(user)
    .set({ emailVerified: true })
    .where(eq(user.email, "admin@robolearn.io"))
    .returning({ id: user.id, email: user.email, emailVerified: user.emailVerified });

  console.log("User verified:", result);
  process.exit(0);
}

main().catch(console.error);
