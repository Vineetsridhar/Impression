import React from "react";
import Group from "./Group";
import { View, ScrollView, StyleSheet, Text } from "react-native";
import { User } from "../helpers/interfaces";

function GroupList({ group }: { group: Group[] }) {
  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        <Group group={group} />
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  contactContainer: {
    flex: 1,
  },
});

export default GroupList;
