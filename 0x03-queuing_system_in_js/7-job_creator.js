#!/usr/bin/node
import { createClient } from 'redis';

async function connectServer() {

  const client = createClient();

  client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

  await client.connect();

  console.log('Redis client connected to the server');
}

connectServer();
