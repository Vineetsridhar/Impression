import React from "react";
import "../Contact/ContactsStyle.tsx";
import PropTypes from "prop-types";

function Contact(props) {
   return (
	<div>
	  <span>{props.name}</span> 
	</div>
   );
}

export default Contact;
