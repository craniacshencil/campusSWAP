# Pending
# 0. General
- [ ] Toast for register and login page instead of messages `frontend` 

# 1. Login
- [ ] Add Toast telling user about why they were redirected to the login page (can be done suing route params see `searchBar` functionality implemented)`frontend`  `backend`
- [ ] Improve styling `frontend` `Tejashri`

# 2. Register
- [ ] Improve styling `frontend` `Tejashri`
- [ ] Take care of possible errors with the phone number
	- [ ] the phonenumber should not be already present in the db `backend` 
	- [ ] phonenumber should be 10 digits `backend`
- [ ] Make sure user first name and last name match `college_students` DB `backend` 

# 3.Buy
- [ ] Use `filterData` to perform query and show matching listings  `backend` `Prathamesh` 
- [ ] Display the matching listings `frontend`
- [ ] Display the searched listing `backend` `Prathamesh`

# 4.Sell
- [ ] Instead of `category` use `courses that need` field that is more accurate
- [ ] Make sure images are lesser than 32Mb and throw error when they are not `frontend`
- [ ] Use 4:3 ratio for cropping (vue-advanced-cropper) `frontend`

# 4.5 Listing Preview
- [ ] Make sure you can go back and make changes in the form provide that option
- [ ] While rendering this make sure the path contains a unique product id
# 5. Home
- [ ] Add proper logo on top `frontend`  `Tejashri`
- [ ] Clicking on each category should redirect to specific search on the buy page `backend` `Prathamesh`
- [ ] Change contact seller to view products on the cards `frontend` `easychange`
# 6. Detailed Listing
- [ ] Wishlist button should actually add the item to wishlist `frontend` `backend`
- [ ] Contact Seller button should link to whatsapp `frontend` `backend`
# 7. User Profile 
- [ ] Users are allowed to upload a bio and image for their avatar `backend` `frontend`
- [ ] Users are allowed to delete their account `backend` `frontend`
- [ ] Users can also see their resources being verified by admin in a similar way `frontend` `backend`
## 7.1 My-listings & Wishlist
- [ ] Add first_name, last-name along with moodleID in brackets for seller info
- [ ] When no listing by user -> include UI
- [ ] Include pagination if possible
- [ ] Make provision for receiving feedback sent by admin
# 8. Admin 
- [ ] Ability to ban users `frontend` `backend`
## 8.1 Moderate Listings
- [ ] Moderate Listings
	- [ ] Every listing has to be moderated by admin before it is seen by users`frontend` `backend`
	- [ ] Send feedback if wrong and add approval to DB if approved
## 8.2 Moderate Resources
- [ ] Moderate Resources
	- [ ] Every resource has to be moderated by admin before it is seen by users`frontend` `backend`
	- [ ] Send feedback if wrong and add approval to DB if approved

# 9. Payment Integration
- [ ] Integrate UPI or whatever it is `frontend` `backend` `Prathamesh`

# 10. Resources section
- [ ] Allow users to create resources catalogues for technologies they are familiar with `frontend` `backend`
- [ ] Display resources to other users `frontend` `backend`
# 11. Recommendation Algo
Can't be using ML here data is too less
- [ ] Probably use history + per user hover over product information + click on product info to recommend products `backend`