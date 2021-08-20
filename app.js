const express = require("express")
const ejs = require("ejs")
const bodyparser = require("body-parser")
const mysql = require("mysql")


const app = express()
app.use(bodyparser.urlencoded({
    extended: false
}))
app.use(bodyparser.json())

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "8897",
    database: "vilas"
})
db.connect()


app.get("/", (req, res) => {
    db.query("select * from student", (err, row) => {
        res.render("index.ejs", {
            students: row
        })
    })
})

app.get("/add_form.ejs", (req, res) => {
    res.render("add_form.ejs")
})

app.post("/InsertData", (req, res) => {
    const details = req.body
    const insertQuery = `insert into student values('${details.rollno1}','${details.firstname1.toUpperCase()}','${details.lastname1.toUpperCase()}','${details.branch1.toUpperCase()}','${details.dob1}','${details.email1}','${details.mobno1}')`
    db.query(insertQuery,(err)=>{
        if(err){}
    })
    res.redirect("/")
})

app.get("/edit_form.ejs/:id", (req, res) => {
    const id = req.params.id
    const editQuery = `select * from student where rollno = ${id}`
    db.query(editQuery, (err, row) => {
        res.render("edit_form.ejs", {
            students: row[0]
        })

    })
})

app.post("/UpdateData/:id", (req, res) => {
    const id = req.params.id
    const details = req.body
    const updateQuery = `update student set ROLLNO = '${details.rollno2}', FIRST_NAME = '${details.firstname2.toUpperCase()}', LAST_NAME = '${details.lastname2.toUpperCase()}', BRANCH = '${details.branch2.toUpperCase()}', DOB = '${details.dob2}', EMAIL = '${details.email2}', MOB_NO = '${details.mobno2}' WHERE ROLLNO = ${id}`
    db.query(updateQuery,(err)=>{
        if(err){}
    })
    res.redirect("/")

})

app.get("/DeleteData/:id", (req, res) => {
    const rollno = req.params.id
    const deleteQuery = `delete from student where rollno = ${rollno}`
    db.query(deleteQuery)
    res.redirect("/")
})

app.listen(5000)