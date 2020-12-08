import React from "react";
import GroupItem from "./GroupItem";
import { View, ScrollView, StyleSheet } from "react-native";
import { Group } from "../helpers/interfaces";

function GroupList({ group }: { group: Group[] }):JSX.Element {
  return (
    <ScrollView contentContainerStyle={{ alignItems: "flex-start" }}>
      <View style={styles.contactContainer}>
        {group.map((group, i) => <GroupItem key={i} group={group} />)}
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
