import React from "react";
import styles from "../Contact/ContactsStyle";
import Contact from "./Contact";
import { View } from "react-native";

interface ContactI {
	id:number,
	name:string
}
function ContactList({contacts}:{contacts:ContactI[]}) {
   return (
	<View>
	   {contacts.map(c => <Contact key={c.id} name={c.name} />)} 
	</View>
   );
}

export default ContactList;
