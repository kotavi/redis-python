import Redis from 'ioredis';

const redis = new Redis();

redis.set('name', 'Tetiana');
redis.get('name', (err, result) => {
    console.log(result);
});