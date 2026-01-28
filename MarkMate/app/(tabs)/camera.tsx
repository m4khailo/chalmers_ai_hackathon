import { View, Text, StyleSheet, Button } from 'react-native';
import { CameraView, useCameraPermissions } from 'expo-camera';
import React from 'react';

export default function CameraScreen() {
    const [permission, requestPermission] = useCameraPermissions();

    if (!permission) {
        return <View />;
    }

    if (!permission.granted) {
        return (
            <View style={styles.center}>
                <Text style={styles.text}>Camera access is required</Text>
                <Button title="Grant Permission" onPress={requestPermission} />
            </View>
        );
    }

    return (
        <View style={styles.container}>
            <CameraView style={styles.camera} />
            <View style={StyleSheet.absoluteFill} pointerEvents="none">
                <Text style={styles.overlaytext}>Make sure that the paper sheet is within the bounding box</Text>
                <View style={styles.frameBox} />
                <View style={styles.controls}>
                    <Button
                        title="Upload Answers"
                        onPress={() => alert('Button Pressed')}
                    />
                </View>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    camera: {
        flex: 1,
    },
    center: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
    },
    text: {
        fontSize: 16,
        marginBottom: 12,
        textAlign: 'center',
    },
    overlaytext: {
        position: 'absolute',
        top: 80,
        width: '100%',
        textAlign: 'center',
        fontSize: 16,
        fontWeight: 'bold',
        color: '#FFFFFF',
    },
    frameBox: {
        position: 'absolute',
        top: '20%',
        left: '10%',
        width: '80%',
        height: '60%',
        borderWidth: 3,
        borderColor: '#00FF00',
        borderRadius: 12,
    },
    controls: {
        position: 'absolute',
        bottom: 40,
        width: '100%',
        alignItems: 'center',
    },
});
