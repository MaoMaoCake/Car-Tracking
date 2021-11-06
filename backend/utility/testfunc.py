def magic(token):
    if token == "12345":
        return {
            "list":[
                {
                    "id": 1,
                    "name": "private",
                    "items":[
                        {
                        "id": 1,
                        "name": "My Tracker",
                        "subitems":[
                            {
                                "id": "my_tracker_1",
                                "name": "My Tracker 1",
                                "color": "red"
                            },
                            {
                                "id": "my_tracker_2",
                                "name": "My Tracker 2",
                                "color": "green"
                            },
                            {
                                "id": "my_tracker_3",
                                "name": "My Tracker 3",
                                "color": "purple"
                            }
                        ]
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Shared",
                    "items":[
                        {
                            "id": 1,
                            "name": "Shared Trackers",
                            "subitems":[
                                {
                                    "id": "share_tracker_1",
                                    "name": "Shared Tracker 1",
                                    "color": "blue"
                                },
                                {
                                    "id": "share_tracker_2",
                                    "name": "Shared Tracker 2",
                                    "color": "brown"
                                },
                                {
                                    "id": "share_tracker_3",
                                    "name": "Shared Tracker 3",
                                    "color": "cyan"
                                }

                            ]
                        },
                    ]
                }
            ]
        }
    else:
        return {
            "list": [
                {
                    "id": 1,
                    "name": "private",
                    "items": [
                        {
                            "id": 1,
                            "name": "My Tracker",
                            "subitems": []
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "Shared",
                    "items": [
                        {
                            "id": 1,
                            "name": "Shared Trackers",
                            "subitems": []
                        },
                    ]
                }
            ]
        }