import React from 'react';
import { Modal, View, Text, TouchableOpacity, StyleSheet, Image } from 'react-native'
import { User } from '../helpers/interfaces';
import { FlatList } from 'react-native-gesture-handler';
import colors from '../../config/colors';
import font from '../../config/font';
import avatar from '../../config/avatar';

interface props {
  isVisible: boolean,
  setModalVisible: React.Dispatch<React.SetStateAction<boolean>>,
  people: User[],
  selectionCallback: (email:string) => void;
}

export default function SelctionModal({ isVisible, setModalVisible, people, selectionCallback }: props) {

  const modalItem = ({item}:{item:User}) => {
    return (
      <TouchableOpacity style={styles.rowContainer} onPress={()=>{selectionCallback(item.email)}} >
      <View style={styles.innerContainer}>
        <Image style={styles.avatarStyle} source={{ uri: item["image"] || avatar }} />

        <View style={{ flexDirection: "column" }}>
          <Text style={[styles.mainTextStyle]}>{item.first_name} {item.last_name}</Text>
          <Text style={styles.textStyle}>{item.email}</Text>
        </View>
      </View>
    </TouchableOpacity>
    )
  }
  return (
    <Modal
      animationType="slide"
      transparent={true}
      visible={isVisible}
    >
      <View style={styles.centeredView}>
        <View style={styles.modalView}>
          <Text style={[styles.mainTextStyle, {fontSize: 24}]}>Select a user</Text>
          <FlatList
            data={people}
            renderItem={modalItem}
            style={styles.listStyle}
          />

          <TouchableOpacity
            style={{ ...styles.openButton, backgroundColor: colors.main }}
            onPress={() => {
              setModalVisible(!isVisible);
            }}
          >
            <Text style={[styles.textStyle, {color:'white', fontSize: 20}]}>Cancel</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  )
}

const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    marginTop: 22
  },
  listStyle:{
    width:'100%',
    marginVertical: 16
  },
  listItem:{
    paddingVertical: 8
  },
  modalView: {
    marginVertical: 20,
    backgroundColor: "white",
    borderRadius: 10,
    paddingVertical: 35,
    alignItems: "center",
    elevation: 5,
    height: 500,
    width: '80%'
  },
  openButton: {
    backgroundColor: "#F194FF",
    borderRadius: 20,
    padding: 10,
    elevation: 2
  },
  textStyle: {
    fontSize: 15,
    color: colors.text,
    fontFamily: font.regular,
  },
  mainTextStyle: {
    fontSize: 20,
    color: colors.text,
    fontFamily: font.bold,

  },
  avatarStyle: {
    height: 40,
    width: 40, 
    borderRadius: 30,
    marginHorizontal: 8
  },
  innerContainer: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'center'
  },
  rowContainer: {
    alignItems: "center",
    display: "flex",
    flexDirection: "row",
    width: '100%',
    justifyContent: 'space-between',
    marginBottom: 8,
    paddingHorizontal: 8
  },
});