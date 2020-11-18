import { StyleSheet } from 'react-native';
import colors from '../../config/colors';

const styles = StyleSheet.create({
    container: {
        display: 'flex',
        margin: 0,
        flexDirection: 'column',
        backgroundColor: colors.background,
        flex: 1
    },
    rowContainer: {
        width: '95%',
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between'
    },
    nameStyle: {
        flex: 1,
        height: 50,
        borderWidth: 1,
        paddingHorizontal: 8,
        borderRadius: 10,
        borderColor: colors.borderColor
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
        width: '95%',
        marginVertical: 8
    },
    avatarStyle: {
        height: 200,
        width: 200,
        borderRadius: 100,
        marginTop: 50
    },
    link: {
        fontSize: 20,
        color: colors.main,
        paddingVertical: 16
    }
})

export default styles
