//define a class (BOT).
class name product
	//
	initiator
		self product name = pname
		self product price = pprice
		
//define a class (BOT).
class product list

	//products related (add/delete/search) in cointainer
	initiator
		self products = []

	//instance of the class.
	function
		//add new products to the list
		add product (append)
		//delete items from existing list
		delete product (delete)
		//search items from existing list
		search product (search)
		
//by using get and post method.
form builder or form method
	
	//request form post method
	if add in request form, follow these valitations and list of form items
	
	//add rules	
		name = request.form []
		price = float(request.form[])
		product is "name and price"
		store in database / in a list
	//after save update list and go back to list
	
	//delete rules
	elif delete in request form, follow these valitations from DB or List
		name = request.form []
		//don't have much know about why for loop is using in delete function
		for loop to select DB and table or List
			product name same as DB or list
			delete form the table or list
//bot 1 complete

//second advance BOT start
	copy of previous BOT
	additional 2 features in advance BOT
	 - search
	 - total in inventory
	 
	//search rules and function
	else as receive a request
		search term should be a form request
		result from DB or list
		
	//product list
		Product name
		product price
		product on hand
		