import redis from 'redis'
import { promisify } from 'util'
client = redis.createClient()

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
const getAsync = promisify(client.get).bind(client)
const displaySchoolValue = async (schoolName) => {
    const value = await getAsync(schoolName)
    console.log(value)
}