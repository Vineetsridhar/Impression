import React from "react";
import Contact from "./Contact";
import { View, ScrollView, StyleSheet } from "react-native";

interface ContactI {
  id: number;
  name: string;
}
function ContactList({ contacts }: { contacts: ContactI[] }) {
  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        {contacts.map((c) => (
          <Contact key={c.id} name={c.name} />
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
