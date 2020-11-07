import React from 'react';
import { View, Text } from 'react-native'
import styles from './ContactsStyle';
import Contact from '../components/Contact';
import ContactList from '../components/ContactList';

interface ContactI {
  id: number,
  name: string,
  email: string
}
interface RecruiterI {
  id: number,
  company: string,
  name: string
}
const contacts: ContactI[] = [
  { id: 1, name: "Chris Mazzei" },
  { id: 2, name: "Stephanie Nieve-Silva" },
  { id: 3, name: "Rami Bazoqa" },
  { id: 4, name: "Vineet Sridhar" },
  { id: 5, name: "Jeff Bezos" },
  { id: 6, name: "Bill Gates" },
];
const recruiters: RecruiterI[] = [
  { id: 1, name: "Recruiter Chris" },
  { id: 2, name: "Recruiter Stephanie" },
  { id: 3, name: "Recruiter Rami" },
  { id: 4, name: "Recruiter Vineet" },
  { id: 5, name: "Recruiter Jeff" },
  { id: 6, name: "Recruiter Bill" },
];
export default function ContactScreen() {
  return (
      <View style={styles.container}> 
		<View style={{flex:2}}>
			<Text style={styles.contactLabel}>Companies</Text>	
			<ContactList contacts={recruiters} />
		</View>
		<View style={{flex:2}}>
			<Text style={styles.contactLabel}>People</Text>
			<ContactList contacts={contacts} />
		</View>
      </View>
  );
}
