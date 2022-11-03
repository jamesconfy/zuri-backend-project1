# Zuri Backend First Project

## Task Description 1

- Setup a server (Host)
- Create an **(GET)** api endoint that returns the following json response:

  { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }

  - SlackUsername should be a **string** datatype and your slack username
  - Backend should be a **boolean** datatype
  - Age should be an  **integer** datatype
  - Bio(description about yourself) should be a **string** datatype

- Push to **GitHub**

**Sample Input:** does not apply
\*\*\*\*None

**Sample Response Format**
{ "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }

**Solution**: [Project](https://first-uajbem42zq-uc.a.run.app/)

## Task Description 2

Using the same server setup from stage one
Create an (POST) api endoint that takes the following sample json:
`html { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }`

- Operation can either be addition, subtraction or mutiplication
- x can be a number and Integer datatype
- y can be a number and Integer datatype

Based on the operation sent, perform a simple arithmetic operation on x and y. Return a response with the result of the operation and your slack username.

format: { “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }
Push to GitHub

`Sample Input: { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }`

`Sample Response Format: { “slackUsername”: String, “result”: Integer, “operation_type”: Enum.value }`
