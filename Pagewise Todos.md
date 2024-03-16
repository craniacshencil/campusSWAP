# 0. General
- [x] Add getter and setters to the persisted-state vuex store plugins
- [x] Get rid of the awkward sidebar
- [x] Get rid of cart does not make sense, or get rid of wishlist
- [x] User badge should redirect to user settings
- [x] Display user's name on the pages
- [x] Add login restriction to the pages
- [x] Add Logout
- [x] When you enter the path to a website in the url, session is terminated, therefore login in both django and vue is terminated (Implemented persistent session state management to solve this)
- [x] Underline the page on which you are in the nav bar.
- [x] Highlight current tab
- [ ] Toast for register and login page instead of messages `frontend` 
# 1. Login
- [ ] Add Toast telling user about why they were redirected to the login page `frontend`  `backend`
- [ ] Improve styling `frontend` `Tejashri`
- [x] Display errors
	- [x] Account does not exist but moodleID valid
	- [x] Make sure all form fields are compulsory
	- [x] Account does not exist because invalid moodleID 
	- [x] incorrect password
- [x] Redirect to a dashboard
- [x] implement form validation
# 2. Register
- [ ] Improve styling `frontend` `Tejashri`
- [ ] Take care of possible errors with the phone number
	- [ ] the phonenumber should not be already present in the db `backend` 
	- [ ] phonenumber should be 10 digits `backend`
- [ ] Make sure user first name and last name match `college_students` DB `backend` 
- [x] Display errors
	- [x] if email/moodleID mismatch
	- [x] if moodleID already registered
	- [x] Invalid moodleId
	- [x] password/reset_password should match
	- [x] password should be strong
	- [x] Make sure all form fields are compulsory
- [x] Redirect to Login
- [x] Create a meta-info table with moodleId as foreign key that keeps track of phonenumber,  the year of the student(include this in the table that prathamesh created containing the entries of AIML students)

# 3. Buy
- [x] display filters only if `buy` page

# 4.Sell
- [x] Change `itemCondition` to select box
- [x] Change `Price` to type = number
- [x] Implement backend for sell 
	- [x] Send form data to django
	- [x] Make sure all form fields are compulsory
	(I ended up manually checking each field if it was empty or not)
	- [x] Store form data in django
	- [x] Ask for phone-number during registration
	- [x] Create table with moodleID as foreign key and add phonenumber there
		(instead of moodleID id has become foreign key because moodleID is not primary key in the auth_user/User table :( )
- [ ] Instead of adding to DB `preview lisiting` should send user to `ListingDetails` `frontend` `easychange`
# 5. Home
- [ ] Add proper logo on top `frontend`  `Tejashri`
- [ ] Search bar should redirect to buy page with relevant info `backend` `Prathamesh`
- [ ] Clicking on each category should redirect to specific search on the buy page `backend` `Prathamesh`
- [ ] Change contact seller to view products on the cards `frontend` `easychange`

# 6. Detailed Listing
- [ ] Galleria component:
	- [ ] Store thumbnails in database too `backend`
	- [ ] Use 4:3 ratio for cropping (vue-advanced-cropper) `frontend`
	- [ ] The buttons near the thumbnail are not working`dunno`
# 7. User Settings
- [ ] Replicate Kaggle, Github style design and use modal/popup/sidebar instead of a whole pages `frontend` 
- [ ] Users should be able to change their password `backend` `easychange`
- [ ] Users are allowed to upload a bio and image for their avatar `backend`