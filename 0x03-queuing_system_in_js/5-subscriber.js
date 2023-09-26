import redis from 'redis'
const client = redis.createClient()

    client.on('error', (err) => {
    console.log('Redis client not connected to the server: ', err.message)
            })
    client.on('connect', () => {
    console.log('Redis client connected to the server')
            })
const subscriber = client.duplicate()

    subscriber.subscribe('holberton school channel', async (message) => {
            if (message == 'KILL_SERVER') {
            await subscriber.unsubscribe()
            await subscriber.quit()
            }
            console.log(message)
            })
