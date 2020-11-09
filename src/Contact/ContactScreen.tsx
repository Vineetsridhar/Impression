import React from "react";
import { View, Text } from "react-native";
import styles from "./ContactsStyle";
import Contact from "../components/Contact";
import ContactList from "../components/ContactList";

interface ContactI {
  id: number;
  name: string;
  email: string;
}
interface RecruiterI {
  id: number;
  company: string;
  name: string;
}
const contacts: ContactI[] = [
  { id: 1, name: "Chris Mazzei", email: "" },
  { id: 2, name: "Stephanie Nieve-Silva", email: "" },
  { id: 3, name: "Rami Bazoqa", email: "" },
  { id: 4, name: "Vineet Sridhar", email: "" },
  { id: 5, name: "Jeff Bezos", email: "" },
  { id: 6, name: "Bill Gates", email: "" },
];
const recruiters: RecruiterI[] = [
  { id: 1, name: "Recruiter Chris", company: "" },
  { id: 2, name: "Recruiter Stephanie", company: "" },
  { id: 3, name: "Recruiter Rami", company: "" },
  { id: 4, name: "Recruiter Vineet", company: "" },
  { id: 5, name: "Recruiter Jeff", company: "" },
  { id: 6, name: "Recruiter Bill", company: "" },
];
export default function ContactScreen() {
  return (
    <View style={styles.container}>
      <View style={{ flex: 2 }}>
        <Text style={styles.contactLabel}>Companies</Text>
        <ContactList contacts={recruiters} />
      </View>
      <View style={{ flex: 2 }}>
        <Text style={styles.contactLabel}>People</Text>
        <ContactList contacts={contacts} />
      </View>
    </View>
  );
}
