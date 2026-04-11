import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then(res => res.json())
      .then(data => setProducts(data));
  }, []);

  return (
    <div>
      <h1>Products</h1>

      {products.map(p => (
        <p key={p.id}>{p.id} - {p.body}</p>
      ))}
    </div>
  );
}

export default App;