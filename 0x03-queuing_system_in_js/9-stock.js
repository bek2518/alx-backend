import { promisify } from 'util';
import { createClient } from 'redis';

const express = require('express');

const app = express();
const hostname = '0.0.0.0';
const port = 1245;

const client = createClient();

const listProducts = [
  {
    itemId: 1, itemName: 'suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  for (const product of listProducts) {
    if (product.itemId === id) {
      return product;
    }
  }
  return null;
}

async function reserveStockById(itemId, stock) {
  return promisify(client.set).bind(client)(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return promisify(client.get).bind(client)(itemId);
}

app.get('/list_products', (req, res) => {
  res.send(JSON.stringify(listProducts));
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
    return;
  }
  item.resevedStock = currentReservedStock || 0;
  res.json(item);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(403).json({ status: 'Product not found' });
  }
  const currentReservedStock = await getCurrentReservedStockById(itemId);
  item.reservedStock = currentReservedStock || 0;
  if ((item.stock - item.reservedStock) < 1) {
    res.status(403).json({ status: 'Not enough stock available', itemId });
    return;
  }
  reserveStockById(itemId, Number(currentReservedStock) + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
