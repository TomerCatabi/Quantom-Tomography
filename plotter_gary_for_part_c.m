videoFileName = '+90+112.5.mp4';
v= VideoReader(videoFileName);
NumFrames = v.NumFrames;
coordinates_A = [176,214,1005,1133];
coordinates_B = [230,260,647,704];
for i=1:1:NumFrames
frame = read(v,i);


%pcolor(frame(400:633,910:1220,1))
D2_A(i)=sum(sum(frame(coordinates_A(1):coordinates_A(2),coordinates_A(3):coordinates_A(4),1)));
D2_B(i)=sum(sum(frame(coordinates_B(1):coordinates_B(2), coordinates_B(3):coordinates_B(4),1)));
%D2(i)=sum(sum(frame(406:647,461:785,1)));
shading flat
%plot(frame(200,:,1))
%[M,I] = max(frame(200,:,1));
%x(i)=I;
%shading flat
%pause(0.05)
%colorbar
i
end
1


plot(D2_A)
plot(D2_B)

FileName = videoFileName(1:end-4);
FileName = strcat(FileName,'.csv');
writematrix(D2_A,FileName);
writematrix(D2_B,FileName,'WriteMode','append');


%pcolor(frame(:,:,1))
%shading flat