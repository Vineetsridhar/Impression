import React from "react";
import GroupItem from "./GroupItem";
import { View, ScrollView, StyleSheet, Text } from "react-native";
import { Group } from "../helpers/interfaces";

function GroupList({ group }: { group: Group[] }) {
  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        {group.map(group => <GroupItem group={group} />)}
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
