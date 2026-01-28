import { Image } from 'expo-image';
import { Platform, StyleSheet } from 'react-native';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';
import React from 'react';

export default function HomeScreen() {
    return (
        <ParallaxScrollView
            headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
            headerImage={
                <Image
                    source={require('@/assets/images/exam-paper.jpg')}
                    style={styles.Logo}
                />
            }>
            <ThemedView style={styles.titleContainer}>
                <ThemedText type="title">Welcome!</ThemedText>
                <HelloWave />
            </ThemedView>
            <ThemedView style={styles.stepContainer}>
                <Link href="/modal">
                    <Link.Trigger>
                        <ThemedText type="subtitle">Step 1: Upload Solved Quiz Answers.</ThemedText>
                    </Link.Trigger>
                </Link>
                <ThemedText>
                    {`Press here to select and upload a file from your device containing the solved quiz answers.`}
                </ThemedText>
            </ThemedView>
            <ThemedView style={styles.stepContainer}>
                <Link href="/camera">
                    <Link.Trigger>
                        <ThemedText type="subtitle">Step 2: Scan Your Students Answers and compare them.</ThemedText>
                    </Link.Trigger>
                </Link>
                <ThemedText>
                    {`When all answers are scanned, you receive a score based on the number of correct answers compared to the uploaded answer key.`}
                </ThemedText>
            </ThemedView>
            <ThemedView style={styles.stepContainer}>
                <ThemedText type="subtitle">Step 3: Receive a Student Score and Save it for Evaluation!</ThemedText>
                <ThemedText>
                    {`When you're done, you receive a score based on the number of correct answers compared to the uploaded answer key.`}
                </ThemedText>
            </ThemedView>
        </ParallaxScrollView>
    );
}

const styles = StyleSheet.create({
    titleContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 8,
    },
    stepContainer: {
        gap: 8,
        marginBottom: 8,
    },
    Logo: {
        height: 300,
        width: '100%',
        alignItems: 'center',
        position: 'absolute',
    },
});
