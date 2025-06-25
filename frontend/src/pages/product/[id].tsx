import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

interface Product {
  product_id: string;
  product_name: string;
  product_brand: string;
  description: string;
  gender: string;
  primary_color: string;
  price_inr: number;
}

const ProductDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const baseUrl = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const res = await fetch(`${baseUrl}/product/${id}`);
        if (!res.ok) {
          throw new Error("Product not found");
        }
        const data = await res.json();
        setProduct(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  if (loading) return <div className="p-4">Loading...</div>;
  if (error) return <div className="p-4 text-red-500">Error: {error}</div>;
  if (!product) return null;

  return (
    <div className="flex-1 flex items-center justify-center">
      <div className="bg-white shadow-lg rounded-2xl p-8 max-w-2xl w-full">
        <div className="mb-6 text-center">
          <h1 className="text-3xl font-bold text-brand mb-2">
            {product.product_name}
          </h1>
          <p className="text-sm text-gray-500 italic">(Demo Page)</p>
        </div>
        <div className="space-y-4 text-lg">
          <p>
            <strong>Brand:</strong> {product.product_brand}
          </p>
          <p>
            <strong>Gender:</strong> {product.gender}
          </p>
          <p>
            <strong>Color:</strong> {product.primary_color}
          </p>
          <p>
            <strong>Price:</strong> ₹{product.price_inr}
          </p>
          <p>
            <strong>Description:</strong> {product.description}
          </p>
        </div>
      </div>
    </div>
  );
};

export default ProductDetailPage;
