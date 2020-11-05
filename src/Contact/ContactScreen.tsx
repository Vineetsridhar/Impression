import React from 'react';
import { View, Text } from 'react-native'
import styles from './ContactsStyle';
import Contact from '../components/Contact';
import ContactList from '../components/ContactList';

interface ContactI {
  id: number,
  name: string
}
const contacts: ContactI[] = [
  { id: 1, name: "Chris Mazzei" },
  { id: 2, name: "Stephanie Nieve-Silva" },
  { id: 3, name: "Rami Bazoqa" },
  { id: 4, name: "Vineet Sridhar" }
];
export default function ContactScreen() {
  return (
      <View style={styles.container}>
        <Text>Contact Screen</Text>
        <ContactList contacts={contacts} />
      </View>
  );
}
