import React, { useState } from "react";
import Contact from "./Contact";
import { View, ScrollView, StyleSheet, Vibration } from "react-native";
import { User } from "../helpers/interfaces";

function ContactList({ contacts }: { contacts: User[] }) {
  const [selected, setSelected] = useState(new Set<number>());
  const [isSelection, setIsSelection] = useState(false);

  const toggleSelection = (index: number) => {
    if (selected.size == 0) {
      Vibration.vibrate(50)
      toggleIsSelected()
    }
    const temp = new Set(selected);
    //Inefficient but mem address has to change for react to rerender
    //Can use a bool array, but determining if empty will be an O(N) operation
    if (temp.has(index)) {
      temp.delete(index)
    } else {
      temp.add(index);
    }
    if (temp.size == 0) {
      toggleIsSelected()
    }
    setSelected(temp)
  }
  const toggleIsSelected = () => {
    setIsSelection(isSelected => !isSelected)
  }

  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        {contacts.map((c, i) => (
          <Contact key={c.email} contact={c} toggleSelection={() => { toggleSelection(i) }} isSelection={isSelection} isSelected={selected.has(i)} />
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
