train_data=[

    {
        "question":"how many clients are there ?",
        "query":"match(c:Client_id) return count(c)"
    },
    {
        "question":"how many clients have the policies ?",
        "query":"match(c:Client_id)-[r:HAS_POLICY]-(p:Policy) return c"
    }
    ,
    {
        "question":"how many sessions are there ?",
        "query":"match(s:Session) return count(s)"
    }
]