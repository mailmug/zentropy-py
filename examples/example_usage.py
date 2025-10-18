#!/usr/bin/env python3
"""
Example usage of the Zentropy client library.

This demonstrates basic operations with the Zentropy server.
"""

from zentropy import Client

def main():
    print("Zentropy Client Example")
    print("=" * 30)
    
    # Connect to Zentropy server
    try:
        # If you have authentication
        # client = Client(host='127.0.0.1', port=6383, password='pass@123')
        
        # Without authentication
        client = Client(host='127.0.0.1', port=6383, password='')
        
        # Test connection
        if client.ping():
            print("✅ Connected to Zentropy server successfully!")
        else:
            print("❌ Connection failed!")
            return
        
        # Basic operations
        print("\n1. Setting values:")
        client.set("name", "Alice")
        client.set("city", "New York")
        client.set("age", "30")
        print("   Set: name, city, age")
        
        print("\n2. Getting values:")
        name = client.get("name")
        city = client.get("city")
        age = client.get("age")
        print(f"   name: {name}")
        print(f"   city: {city}")
        print(f"   age: {age}")
        
        print("\n3. Checking existence:")
        exists = client.exists("name")
        print(f"   Key 'name' exists: {exists}")
        
        print("\n4. Deleting a key:")
        deleted = client.delete("age")
        print(f"   Deleted 'age': {deleted}")
        
        # Verify deletion
        age_after_delete = client.get("age")
        print(f"   'age' after deletion: {age_after_delete}")
        
        # Using context manager (recommended)
        print("\n5. Using context manager:")
        with Client(host='127.0.0.1', port=6383) as client_ctx:
            client_ctx.set("temp_key", "temp_value")
            temp_value = client_ctx.get("temp_key")
            print(f"   temp_value: {temp_value}")
            # Automatically closed when exiting the context
        
        print("\n🎉 All operations completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Make sure the Zentropy server is running on 127.0.0.1:6383")

if __name__ == "__main__":
    main()