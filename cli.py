import argparse
from services.marketplace.marketplace_manager import MarketplaceManager
from services.user_manager import UserManager  # Make sure this import is correct

def main():
    parser = argparse.ArgumentParser(description="Command-line interface for Marketplace and User Management")
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Marketplace commands
    marketplace_parser = subparsers.add_parser("marketplace", help="Marketplace commands")
    marketplace_subparsers = marketplace_parser.add_subparsers(dest="marketplace_command", help="Marketplace actions")

    add_item_parser = marketplace_subparsers.add_parser("add_item", help="Add an item")
    add_item_parser.add_argument("item_name", help="Name of the item")
    add_item_parser.add_argument("price", type=int, help="Price of the item")

    remove_item_parser = marketplace_subparsers.add_parser("remove_item", help="Remove an item")
    remove_item_parser.add_argument("item_name", help="Name of the item")

    update_item_parser = marketplace_subparsers.add_parser("update_item", help="Update item price")
    update_item_parser.add_argument("item_name", help="Name of the item")
    update_item_parser.add_argument("price", type=int, help="New price of the item")

    view_item_parser = marketplace_subparsers.add_parser("view_item", help="View an item")
    view_item_parser.add_argument("item_name", help="Name of the item")

    # User management commands
    user_parser = subparsers.add_parser("user", help="User commands")
    user_subparsers = user_parser.add_subparsers(dest="user_command", help="User actions")

    add_user_parser = user_subparsers.add_parser("add_user", help="Add a user")
    add_user_parser.add_argument("username", help="Username of the user")
    add_user_parser.add_argument("initial_balance", type=int, help="Initial balance for the user")

    args = parser.parse_args()

    if args.command == "marketplace":
        marketplace_manager = MarketplaceManager()
        if args.marketplace_command == "add_item":
            print(marketplace_manager.add_item(args.item_name, args.price))
        elif args.marketplace_command == "remove_item":
            print(marketplace_manager.remove_item(args.item_name))
        elif args.marketplace_command == "update_item":
            print(marketplace_manager.update_item(args.item_name, args.price))
        elif args.marketplace_command == "view_item":
            item = marketplace_manager.get_item(args.item_name)
            if item:
                print(f"Item: {args.item_name}, Price: {item}")
            else:
                print(f"Item '{args.item_name}' not found.")

    elif args.command == "user":
        user_manager = UserManager()
        if args.user_command == "add_user":
            if args.username and args.initial_balance:
                print(user_manager.add_user(args.username, args.initial_balance))
            else:
                print("Error: Username and initial balance are required to add a user.")

if __name__ == "__main__":
    main()

