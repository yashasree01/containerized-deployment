import React from 'react';
import { useState, useEffect } from 'react';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

interface Item {
  id: string;
  name: string;
  description?: string;
  price: number;
  quantity: number;
}

function App() {
  const [items, setItems] = useState<Item[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await fetch(`${API_URL}/items`);
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();
      setItems(data);
      setError(null);
    } catch (err) {
      setError('Failed to load items');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="p-8">Loading...</div>;
  if (error) return <div className="p-8 text-red-500">{error}</div>;

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">Containerized App</h1>
      <div className="grid gap-4">
        {items.map((item) => (
          <div key={item.id} className="bg-white p-4 rounded shadow">
            <h3 className="font-semibold">{item.name}</h3>
            <p className="text-gray-600">{item.description}</p>
            <p className="text-blue-600 font-bold">${item.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
