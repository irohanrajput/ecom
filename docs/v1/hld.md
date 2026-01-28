# Order Processing System - High Level Design

## Architecture Overview
```
Browser
  |
  | HTTP (REST) + SSE
  v
FastAPI (API Gateway + Order Service)
  |
  | write / read
  v
PostgreSQL  <─── Redis (cache)
  |
  | enqueue tasks
  v
RabbitMQ (tasks_queue)
  |
  | consume
  v
Universal Worker
  |
  | side effects + state updates
  v
PostgreSQL + Redis Pub/Sub
  |
  | SSE
  v
Browser
```

## Order State Machine
```
CREATED
  ↓
PROCESSING
  ↓
CONFIRMED ──→ SHIPPED (later)
  ↓
FAILED / CANCELLED
```

## Rules

- Only worker changes state after CREATED
- CONFIRMED is the only "success"
- No email/SMS before CONFIRMED
