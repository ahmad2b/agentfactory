### Core Concept
Dependency injection organizes code that needs shared resources. `Depends()` wrapper calls functions at request time (not import time). Yield dependencies enable cleanup (session.close after request). Dependencies chain together—`get_current_user` depends on both `oauth2_scheme` and `get_session`.

### Key Mental Models
- **Inversion of control**: Endpoints declare what they need; framework provides it
- **Request-scoped**: Dependencies cached per request, called once even if used multiple times
- **Yield for cleanup**: Code after `yield` runs after endpoint completes (even on exception)
- **Dependency graph**: Visualize as tree—FastAPI resolves automatically

### Critical Patterns
- Simple dependency: `def get_settings() -> Settings: return Settings()`
- Yield dependency: `yield session` then `session.close()` in finally
- Chained: `get_admin_user` depends on `get_current_user` depends on `get_session`
- Class-based: `service: TaskService = Depends()` uses `__init__` parameters
- Testing override: `app.dependency_overrides[get_session] = get_test_session`

### AI Collaboration Keys
- Prompt 1: Request-scoped caching—FastAPI dependency caching behavior
- Prompt 2: Background tasks—dependencies with different lifecycles
- Prompt 3: Conditional dependencies—optional authentication for public/private data

### Common Mistakes
- Creating resources without cleanup (yield with finally block)
- Calling function at import: `= get_session()` vs `= Depends(get_session)`
- Not clearing overrides after tests
- Forgetting Depends() wrapper entirely

### Connections
- **Builds on**: JWT Authentication (Lesson 9)
- **Leads to**: Middleware & CORS (Lesson 11)
