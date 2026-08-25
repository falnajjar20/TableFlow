# TableFlow

## Product idea

TableFlow is a mobile-first restaurant payment website.

A guest scans a QR code at their table, views the bill, chooses what
they want to pay, adds a tip, completes a test payment, and receives
a digital receipt.

Restaurant staff can create bills and monitor payment progress.

## Users

### Guest

- Scans the table QR code
- Views the bill
- Splits the bill
- Adds a tip
- Pays using a test payment
- Receives a receipt

### Restaurant staff

- Signs in securely
- Creates tables and QR codes
- Opens and updates bills
- Watches payment progress
- Closes paid bills

## MVP features

- Restaurant and staff accounts
- Restaurant tables
- Unique table QR codes
- Open restaurant bills
- Bill items
- Pay the entire bill
- Split equally
- Select individual items
- Pay a custom amount
- Add a tip
- Stripe test payment
- Digital receipt
- Restaurant dashboard

## Not included in the MVP

- Real-money production payments
- Real POS integrations
- NFC or SoftPOS
- Customer mobile application
- Loyalty program
- Food ordering
- Multiple restaurant branches
- Refund and chargeback management

## Important rules

- Money is stored as integer cents
- The server calculates every payment amount
- Card information is never stored
- Stripe test mode is used
- Two guests cannot pay for the same item
- Payment completion is confirmed by a webhook
- Every restaurant can access only its own data

## MVP success scenario

Three friends share one restaurant bill.

1. Friend A selects and pays for their items.
2. Friend B pays one-third of the remaining balance.
3. Friend C pays the remainder.
4. The restaurant dashboard shows each payment.
5. The bill becomes paid without being overpaid.
