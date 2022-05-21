class Filter:
    def getRentFilter(self):
        filter =  {
            "filter": {
                "and": [
                    {
                        "property": "title",
                        "rich_text": {
                            "equals": "Collect And Pay For Rent"
                        }
                    },
                    {
                        "property": "Status",
                        "select": {
                            "equals": "Required"
                        }
                    }
                ]
            }
        }

        return filter

    def getCreditCardFilter(self):
        filter =  {
            "filter": {
                "and": [
                    {
                        "property": "title",
                        "rich_text": {
                            "equals": "Pay For Credit Card"
                        }
                    },
                    {
                        "property": "Status",
                        "select": {
                            "equals": "Required"
                        }
                    }
                ]
            }
        }

        return filter
    
    def getUCIFilter(self):
        filter =  {
            "filter": {
                "and": [
                    {
                        "property": "title",
                        "rich_text": {
                            "equals": "Renew UCI Email"
                        }
                    },
                    {
                        "property": "Status",
                        "select": {
                            "equals": "Required"
                        }
                    }
                ]
            }
        }

        return filter