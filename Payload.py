import Constants
from datetime import datetime

class Payload:
    def getCurrentTime(self):
        currentDay = datetime.today()
        return currentDay
    
    def getPayRentTime(self):
        day = self.getCurrentTime()
        modifiedDate = day.replace(day=29)
        return modifiedDate.strftime("%Y-%m-%d")

    def getCreditCardTime(self):
        day = self.getCurrentTime()
        modifiedDate = day.replace(day=15)
        return modifiedDate.strftime("%Y-%m-%d")

    def getRentPayload(self):
        payload = {
            "parent": {"database_id": Constants.BULLETIN_BOARD},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Collect And Pay For Rent"
                            }
                        }
                    ]
                },
                "Status": {
                    "select": {
                        "name": "Required",
                    }
                },
                "Difficulty": {
                    "select": {
                        "name": "2",
                    }
                },
                "Tags": {
                    "relation": [
                        {
                            "id": "5f07cdd9516a4e07821ead9338489227"
                        }
                    ]
                },
                "Do Date": {
                    "date": {
                        "start": self.getPayRentTime()
                    }
                },
            }
        }

        return payload
    
    def getCreditCardPayload(self):
        payload = {
            "parent": {"database_id": Constants.BULLETIN_BOARD},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Pay For Credit Card"
                            }
                        }
                    ]
                },
                "Status": {
                    "select": {
                        "name": "Required",
                    }
                },
                "Difficulty": {
                    "select": {
                        "name": "1",
                    }
                },
                "Tags": {
                    "relation": [
                        {
                            "id": "87efd56a283248baa4d1a45948c6bcaa"
                        }
                    ]
                },
                "Do Date": {
                    "date": {
                        "start": self.getCreditCardTime()
                    }
                },
            }
        }

        return payload
    
    def getUCIEmailPayload(self):
        payload = {
            "parent": {"database_id": Constants.BULLETIN_BOARD},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Renew UCI Email"
                            }
                        }
                    ]
                },
                "Status": {
                    "select": {
                        "name": "Required",
                    }
                },
                "Difficulty": {
                    "select": {
                        "name": "1",
                    }
                },
                "Tags": {
                    "relation": [
                        {
                            "id": "87efd56a283248baa4d1a45948c6bcaa"
                        }
                    ]
                },
                "Do Date": {
                    "date": {
                        "start": self.getCreditCardTime()
                    }
                },
            }
        }

        return payload
