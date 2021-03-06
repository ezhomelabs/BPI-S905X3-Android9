/*
 * Copyright (C) 2018 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.android.tradefed.device.metric;

import com.android.tradefed.device.DeviceNotAvailableException;
import com.android.tradefed.device.ITestDevice;
import com.android.tradefed.log.LogUtil.CLog;
import com.android.tradefed.result.FileInputStreamSource;
import com.android.tradefed.result.InputStreamSource;
import com.android.tradefed.result.LogDataType;
import com.google.common.io.Files;
import java.io.File;
import java.io.IOException;

/**
 * A {@link ScheduledDeviceMetricCollector} to collect audio and system memory heaps at regular
 * intervals.
 */
public class IonHeapInfoMetricCollector extends ScheduledDeviceMetricCollector {
    public IonHeapInfoMetricCollector() {
        setTag("ion");
    }

    @Override
    void collect(ITestDevice device, DeviceMetricData runData) throws InterruptedException {
        collectIonAudio(device);
        collectIonSystem(device);
    }

    private void collectIonAudio(ITestDevice device) {
        try {
            CLog.i("Running ionheap audio collector...");
            String outputFileName =
                    String.format("%s/ion-audio-%s", createTempDir(), getFileSuffix());
            File outputFile = saveProcessOutput(device, "cat /d/ion/heaps/audio", outputFileName);
            try (InputStreamSource source = new FileInputStreamSource(outputFile, true)) {
                getInvocationListener()
                        .testLog(
                                Files.getNameWithoutExtension(outputFile.getName()),
                                LogDataType.TEXT,
                                source);
            }
        } catch (DeviceNotAvailableException | IOException e) {
            CLog.e(e);
        }
    }

    private void collectIonSystem(ITestDevice device) {
        try {
            CLog.i("Running ionheap system collector...");
            String outputFileName =
                    String.format("%s/ion-system-%s", createTempDir(), getFileSuffix());
            File outputFile = saveProcessOutput(device, "cat /d/ion/heaps/system", outputFileName);
            try (InputStreamSource source = new FileInputStreamSource(outputFile, true)) {
                getInvocationListener()
                        .testLog(
                                Files.getNameWithoutExtension(outputFile.getName()),
                                LogDataType.TEXT,
                                source);
            }
        } catch (DeviceNotAvailableException | IOException e) {
            CLog.e(e);
        }
    }
}
