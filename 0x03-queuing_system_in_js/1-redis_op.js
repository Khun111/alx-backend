import redis from 'redis'
const client = redis.createClient()

    client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err.message)
            })
    client.on('connect', () => {
    console.log('Redis client connected to the server')
    displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
            })
const setNewSchool = (schoolName, value) => {
client.set(schoolName, value, redis.print)
}
const displaySchoolValue = (schoolName) => {
    client.get(displaySchoolValue, (err, result) => {
    if (err) console.log(err)
    console.log(result)
            })
}
