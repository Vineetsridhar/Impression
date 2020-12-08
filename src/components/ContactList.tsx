import React from "react";
import Contact from "./Contact";
import { View, ScrollView, StyleSheet, Vibration } from "react-native";
import { User } from "../helpers/interfaces";
interface props {
  contacts: User[],
  setButtonVisible: React.Dispatch<React.SetStateAction<boolean>>,
  selected: Set<number>;
  setSelected: React.Dispatch<React.SetStateAction<Set<number>>>,
  isSelection: boolean;
  setIsSelection: React.Dispatch<React.SetStateAction<boolean>>,
}
function ContactList({ contacts, setButtonVisible, selected, setSelected, isSelection, setIsSelection }: props):JSX.Element {

  const toggleSelection = (index: number) => {
    if (selected.size == 0) {
      Vibration.vibrate(50)
      toggleIsSelected()
      setButtonVisible(true)
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
    setButtonVisible(false)
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
