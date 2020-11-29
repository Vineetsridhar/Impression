import React from 'react'
import ContactList from '../components/ContactList'
import { Text, StyleSheet, ScrollView } from 'react-native'
import colors from '../../config/colors'
import font from '../../config/font'

export default function GroupDetail({ navigation, route }: any) {
    return (
        <ScrollView style={styles.container}>
            <Text style={styles.title}>{route.params.name}</Text>
            <ContactList
                contacts={route.params.data}
                setButtonVisible={() => { }}
                selected={new Set<number>()}
                setSelected={() => { }}
                isSelection={false}
                setIsSelection={() => { }} />
        </ScrollView>
    )
}

const styles = StyleSheet.create({
    title: {
        width: '100%',
        textAlign: 'center',
        fontSize: 30,
        fontFamily: font.bold,
        color: colors.text,
        marginVertical: 16
    },
    container: { backgroundColor: colors.background, flex: 1 }
})