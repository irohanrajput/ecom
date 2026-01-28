# Order Processing System - Low Level Design (LLD)

## 1️⃣ Database Schema (PostgreSQL)

### orders
```sql
orders (
  id UUID PK,
  user_id UUID,
  status VARCHAR,         -- CREATED | PROCESSING | CONFIRMED | FAILED
  total_amount INT,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)
```

### order_events (optional but recommended)
```sql
order_events (
  id UUID PK,
  order_id UUID,
  event_type VARCHAR,
  created_at TIMESTAMP
)
```

## 2️⃣ RabbitMQ

### Exchange
* Default exchange (v1 simplicity)

### Queue
```
tasks_queue
```

### Message Format (TASK ENVELOPE)
```json
{
  "task_id": "uuid",
  "task_type": "charge_payment",
  "order_id": "uuid",
  "payload": {
    "amount": 1999
  }
}
```

✅ `task_type` is mandatory  
✅ `task_id` is mandatory (idempotency)

## 3️⃣ Universal Worker (LLD)

### Internal Dispatcher
```python
TASK_HANDLERS = {
  "charge_payment": handle_payment,
  "reserve_inventory": handle_inventory,
  "send_email": handle_email
}
```

### Processing Rules
* One message → one handler
* ACK only after success
* On failure:
  * Update order state
  * Emit compensation event
  * ACK (don't poison queue)

## 4️⃣ Redis

### Cache
```
order:{order_id} → latest order snapshot
```

### Pub/Sub
```
order_status_updates
```

**Message:**
```json
{
  "order_id": "uuid",
  "status": "PROCESSING"
}
```

## 5️⃣ SSE (FastAPI)

### Endpoint
```
GET /orders/{order_id}/events
```

### Flow
* FastAPI subscribes to Redis Pub/Sub
* Streams events to client
* Client updates UI live
