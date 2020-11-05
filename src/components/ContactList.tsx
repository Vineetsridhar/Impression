import React from "react";
import "../Contact/ContactsStyle.tsx";
import Contact from "./Contact.tsx";
function ContactList(props) {
   return (
	<div>
	   {props.contacts.map(c => <Contact key={c.id} name={c.name} />)} 
	</div>
   );
}

export default ContactList;
