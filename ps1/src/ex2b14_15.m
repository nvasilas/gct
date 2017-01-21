function ex2b14_15()
    x = 0:0.1:2*pi;
    y = 0:0.1:2*pi;
    [X, Y] = meshgrid(x, y);
    I = cos(X).*sin(2.*Y);
    J = sin(X + 2.*Y);
    figure(1);
    quiver(X, Y, I, J);

    h_I = -Y;
    h_J = X;
    %figure(2);
    %quiver(X, Y, h_I, h_J);
end
