function GT(user_token){
    var json = {
        list:[
            {
                id: 1,
                name: "private",
                items:[
                    {
                    id: 1,
                    name: "My Tracker",
                    subitems:[
                        {
                            id: 1,
                            name: "My Tracker 1",
                            color: "red"
                        },
                        {
                            id: 2,
                            name: "My Tracker 2",
                            color: "green"
                        }
                    ]
                    }
                ]
            },
            {
                id: 2,
                name: "Shared",
                items:[
                    {
                        id: 1,
                        name: "Shared Trackers",
                        subitems:[
                            {
                                id: 1,
                                name: "Shared Tracker 1",
                                color: "blue"
                            },
                            {
                                id: 2,
                                name: "Shared Tracker 2",
                                color: "yellow"
                            }
                        ]
                    }, 
                ]
            }
        ]
    };
    return json;
}
export default GT