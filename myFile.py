import stripe

# Set your Stripe API key
stripe.api_key = 'rk_live_5hTOJGTdSoHZ2V5GJGPYTZNR'

def create_customer(email):
    """Create a new customer."""
    customer = stripe.Customer.create(
        email=email,
    )
    return customer

def create_charge(customer_id, amount, currency='usd'):
    """Create a charge for a customer."""
    charge = stripe.Charge.create(
        customer=customer_id,
        amount=amount,
        currency=currency,
        description='Example Charge',
    )
    return charge

if __name__ == "__main__":
    # Create a new customer
    email = input("Enter customer email: ")
    customer = create_customer(email)
    print("Customer created:")
    print(customer)

    # Charge the customer
    amount = int(input("Enter amount to charge (in cents): "))
    charge = create_charge(customer.id, amount)
    print("Charge created:")
    print(charge)
