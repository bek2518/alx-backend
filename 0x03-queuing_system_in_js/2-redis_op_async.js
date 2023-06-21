import { createClient } from 'redis';

import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));
const get = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    console.log('Reply: ', reply);
  });
}

async function displaySchoolValue(schoolName) {
  const value = await get(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
