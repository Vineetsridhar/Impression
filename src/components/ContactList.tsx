import React from "react";
import Contact from "./Contact";
import { View, ScrollView, StyleSheet } from "react-native";
import { User } from "../helpers/interfaces";

function ContactList({ contacts }: { contacts: User[] }) {
  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        {contacts.map((c) => (
          <Contact key={c.email} contact={c} />
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  contactContainer: {
    flex: 1,
  },
});

export default ContactList;
