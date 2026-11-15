$version: "2.0"

namespace com.mycompany.todo

use aws.protocols#restJson1

@restJson1
service TodoService {
    version: "2026-11-15"
    operations: [
        CreateTodo
        ListTodos
        ToggleTodo
        DeleteTodo
    ]
}

structure Todo {
    @required
    id: String

    @required
    title: String

    @required
    completed: Boolean
}

list TodoList {
    member: Todo
}

@error("client")
@httpError(404)
structure NotFoundError {
    @required
    message: String
}

@http(method: "POST", uri: "/todos", code: 201)
operation CreateTodo {
    input := {
        @required
        title: String
    }

    output := {
        @httpPayload
        @required
        todo: Todo
    }
}

@readonly
@paginated(inputToken: "nextToken", outputToken: "nextToken", pageSize: "maxResults", items: "todos")
@http(method: "GET", uri: "/todos", code: 200)
operation ListTodos {
    input := {
        @httpQuery("nextToken")
        nextToken: String

        @httpQuery("maxResults")
        maxResults: Integer
    }

    output := {
        @required
        todos: TodoList

        nextToken: String
    }
}

@http(method: "PATCH", uri: "/todos/{id}/toggle", code: 200)
operation ToggleTodo {
    input := {
        @httpLabel
        @required
        id: String
    }

    output := {
        @httpPayload
        @required
        todo: Todo
    }

    errors: [
        NotFoundError
    ]
}

@idempotent
@http(method: "DELETE", uri: "/todos/{id}", code: 204)
operation DeleteTodo {
    input := {
        @httpLabel
        @required
        id: String
    }

    output := {}

    errors: [
        NotFoundError
    ]
}
