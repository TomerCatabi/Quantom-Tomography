%filename should be edited according to the video name that were saved on your local computer
v= VideoReader('2024-07-14 01-22-17.mp4');
%Final value of i shoud be changed to the number of frames in the video (30 frames in a second -> 30*number_of_seconds)
for i=1:1:30*134
frame = read(v,i);

%D2 sums on the specific coordinates given (yi:yf, xi:xf)
%pcolor(frame(400:633,910:1220,1))
D2(i)=sum(sum(frame(201:242,1022:1124,1)));
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


plot(D2) 

% one can uncomment the following lines in order to get a matlab image of the firs frame and extruct the y and x coordinates given
%pcolor(frame(:,:,1))
%shading flat
