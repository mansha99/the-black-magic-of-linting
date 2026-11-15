Prompt:
"Act as an API architect. Write a complete, valid Smithy 2.0 IDL contract for a RESTful Todo List service using the @restJson1 protocol.
Requirements:
• Namespace: example.todo
• Data Model: Define a Todo structure containing id (@required String), title (@required String), and completed (@required Boolean).
• Operations & HTTP Bindings:
	1. CreateTodo (POST /todos): Accepts a title in the payload and returns the created Todo.
	2. ListTodos (GET /todos): Returns a list of Todo structures.
	3. ToggleTodo (PATCH /todos/{id}/toggle): Toggles the completed status and returns the updated Todo.
	4. DeleteTodo (DELETE /todos/{id}): Deletes the specified item and returns a 204 No Content status.
• Errors: Include a basic NotFoundError (@error("client"), @httpError(404)) and attach it to operations that look up an existing id.
Output only the .smithy file content without extra boilerplate."