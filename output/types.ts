type MyQueryResultBooks = {
    title: string
    author: string
}

type MyQueryResultUsers = {
    id: number
    name: string
    friends: number[] | undefined
}

type MyQueryResult = {
    books: MyQueryResultBooks[]
    users: MyQueryResultUsers[]
}