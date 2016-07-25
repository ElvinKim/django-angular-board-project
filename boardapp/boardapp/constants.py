#Basic Info
MAIN_URL = "http://localhost:8000"

#STS
SUCCESS = 1000

#STS - ERROR

#1~99 : Critical Error
ERR_DB_CONNECT = 1

#100~199 : User Side Error
ERR_USER_PARAM = 100

#201~299 : Database Error
ERR_DB_SELECT = 200
ERR_DB_INSERT = 201
ERR_DB_UPDATE = 202

#MSG
MSG = {
    SUCCESS : "Success",

    ERR_USER_PARAM : "User didn't send enough parameters",
    ERR_DB_SELECT : "Database Select Error",
    ERR_DB_INSERT : "Database Insert Error",
    ERR_DB_UPDATE : "Database Update Error",
}

