from cffi import FFI

ffi = FFI()

ffi.set_source('_graphene_cffi', '#include <graphene-1.0/graphene.h>', libraries=['graphene-1.0'])

ffi.cdef('''
    // graphene-types.h
    typedef struct _graphene_vec2_t {...;} graphene_vec2_t;
    typedef struct _graphene_vec3_t {...;} graphene_vec3_t;
    typedef struct _graphene_vec4_t {...;} graphene_vec4_t;
    typedef struct _graphene_matrix_t {...;} graphene_matrix_t;
    typedef struct _graphene_point_t {...;} graphene_point_t;
    typedef struct _graphene_size_t {...;} graphene_size_t;
    typedef struct _graphene_rect_t {...;} graphene_rect_t;
    typedef struct _graphene_point3d_t {...;} graphene_point3d_t;
    typedef struct _graphene_quad_t {...;} graphene_quad_t;
    typedef struct _graphene_quaternion_t {...;} graphene_quaternion_t;
    typedef struct _graphene_euler_t {...;} graphene_euler_t;
    typedef struct _graphene_plane_t {...;} graphene_plane_t;
    typedef struct _graphene_frustum_t {...;} graphene_frustum_t;
    typedef struct _graphene_sphere_t {...;} graphene_sphere_t;
    typedef struct _graphene_box_t {...;} graphene_box_t;
    typedef struct _graphene_triangle_t {...;} graphene_triangle_t;
    typedef struct _graphene_ray_t {...;} graphene_ray_t;

    typedef enum {
        GRAPHENE_EULER_ORDER_DEFAULT = -1,
        GRAPHENE_EULER_ORDER_XYZ = 0,
        GRAPHENE_EULER_ORDER_YZX,
        GRAPHENE_EULER_ORDER_ZXY,
        GRAPHENE_EULER_ORDER_XZY,
        GRAPHENE_EULER_ORDER_YXZ,
        GRAPHENE_EULER_ORDER_ZYX
    } graphene_euler_order_t;

    // graphene-vec2.h
    graphene_vec2_t *       graphene_vec2_alloc             (void);
    void                    graphene_vec2_free              (graphene_vec2_t       *v);
    graphene_vec2_t *       graphene_vec2_init              (graphene_vec2_t       *v,
                                                             float                  x,
                                                             float                  y);
    graphene_vec2_t *       graphene_vec2_init_from_vec2    (graphene_vec2_t       *v,
                                                             const graphene_vec2_t *src);
    graphene_vec2_t *       graphene_vec2_init_from_float   (graphene_vec2_t       *v,
                                                             const float           *src);
    void                    graphene_vec2_to_float          (const graphene_vec2_t *v,
                                                             float                 *dest);
    void                    graphene_vec2_add               (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_subtract          (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_multiply          (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_divide            (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    float                   graphene_vec2_dot               (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b);
    float                   graphene_vec2_length            (const graphene_vec2_t *v);
    void                    graphene_vec2_normalize         (const graphene_vec2_t *v,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_scale             (const graphene_vec2_t *v,
                                                             float                  factor,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_negate            (const graphene_vec2_t *v,
                                                             graphene_vec2_t       *res);
    bool                    graphene_vec2_near              (const graphene_vec2_t *v1,
                                                             const graphene_vec2_t *v2,
                                                             float                  epsilon);
    bool                    graphene_vec2_equal             (const graphene_vec2_t *v1,
                                                             const graphene_vec2_t *v2);
    void                    graphene_vec2_min               (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec2_max               (const graphene_vec2_t *a,
                                                             const graphene_vec2_t *b,
                                                             graphene_vec2_t       *res);
    float                   graphene_vec2_get_x             (const graphene_vec2_t *v);
    float                   graphene_vec2_get_y             (const graphene_vec2_t *v);
    const graphene_vec2_t * graphene_vec2_zero              (void);
    const graphene_vec2_t * graphene_vec2_one               (void);
    const graphene_vec2_t * graphene_vec2_x_axis            (void);
    const graphene_vec2_t * graphene_vec2_y_axis            (void);
    
    // graphene-vec3.h
    graphene_vec3_t *       graphene_vec3_alloc             (void);
    void                    graphene_vec3_free              (graphene_vec3_t       *v);
    graphene_vec3_t *       graphene_vec3_init              (graphene_vec3_t       *v,
                                                             float                  x,
                                                             float                  y,
                                                             float                  z);
    graphene_vec3_t *       graphene_vec3_init_from_vec3    (graphene_vec3_t       *v,
                                                             const graphene_vec3_t *src);
    graphene_vec3_t *       graphene_vec3_init_from_float   (graphene_vec3_t       *v,
                                                             const float           *src);
    void                    graphene_vec3_to_float          (const graphene_vec3_t *v,
                                                             float                 *dest);
    void                    graphene_vec3_add               (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_subtract          (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_multiply          (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_divide            (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_cross             (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    float                   graphene_vec3_dot               (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b);
    float                   graphene_vec3_length            (const graphene_vec3_t *v);
    void                    graphene_vec3_normalize         (const graphene_vec3_t *v,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_scale             (const graphene_vec3_t *v,
                                                             float                  factor,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_negate            (const graphene_vec3_t *v,
                                                             graphene_vec3_t       *res);
    bool                    graphene_vec3_equal             (const graphene_vec3_t *v1,
                                                             const graphene_vec3_t *v2);
    bool                    graphene_vec3_near              (const graphene_vec3_t *v1,
                                                             const graphene_vec3_t *v2,
                                                             float                  epsilon);
    void                    graphene_vec3_min               (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_max               (const graphene_vec3_t *a,
                                                             const graphene_vec3_t *b,
                                                             graphene_vec3_t       *res);
    float                   graphene_vec3_get_x             (const graphene_vec3_t *v);
    float                   graphene_vec3_get_y             (const graphene_vec3_t *v);
    float                   graphene_vec3_get_z             (const graphene_vec3_t *v);
    void                    graphene_vec3_get_xy            (const graphene_vec3_t *v,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec3_get_xy0           (const graphene_vec3_t *v,
                                                             graphene_vec3_t       *res);
    void                    graphene_vec3_get_xyz0          (const graphene_vec3_t *v,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec3_get_xyz1          (const graphene_vec3_t *v,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec3_get_xyzw          (const graphene_vec3_t *v,
                                                             float                  w,
                                                             graphene_vec4_t       *res);
    const graphene_vec3_t * graphene_vec3_zero              (void);
    const graphene_vec3_t * graphene_vec3_one               (void);
    const graphene_vec3_t * graphene_vec3_x_axis            (void);
    const graphene_vec3_t * graphene_vec3_y_axis            (void);
    const graphene_vec3_t * graphene_vec3_z_axis            (void);
    
    // graphene-vec4.h
    graphene_vec4_t *       graphene_vec4_alloc             (void);
    void                    graphene_vec4_free              (graphene_vec4_t       *v);
    graphene_vec4_t *       graphene_vec4_init              (graphene_vec4_t       *v,
                                                             float                  x,
                                                             float                  y,
                                                             float                  z,
                                                             float                  w);
    graphene_vec4_t *       graphene_vec4_init_from_vec4    (graphene_vec4_t       *v,
                                                             const graphene_vec4_t *src);
    graphene_vec4_t *       graphene_vec4_init_from_vec3    (graphene_vec4_t       *v,
                                                             const graphene_vec3_t *src,
                                                             float                  w);
    graphene_vec4_t *       graphene_vec4_init_from_vec2    (graphene_vec4_t       *v,
                                                             const graphene_vec2_t *src,
                                                             float                  z,
                                                             float                  w);
    graphene_vec4_t *       graphene_vec4_init_from_float   (graphene_vec4_t       *v,
                                                             const float           *src);
    void                    graphene_vec4_to_float          (const graphene_vec4_t *v,
                                                             float                 *dest);
    void                    graphene_vec4_add               (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_subtract          (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_multiply          (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_divide            (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    float                   graphene_vec4_dot               (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b);
    float                   graphene_vec4_length            (const graphene_vec4_t *v);
    void                    graphene_vec4_normalize         (const graphene_vec4_t *v,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_scale             (const graphene_vec4_t *v,
                                                             float                  factor,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_negate            (const graphene_vec4_t *v,
                                                             graphene_vec4_t       *res);
    bool                    graphene_vec4_equal             (const graphene_vec4_t *v1,
                                                             const graphene_vec4_t *v2);
    bool                    graphene_vec4_near              (const graphene_vec4_t *v1,
                                                             const graphene_vec4_t *v2,
                                                             float                  epsilon);
    void                    graphene_vec4_min               (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    void                    graphene_vec4_max               (const graphene_vec4_t *a,
                                                             const graphene_vec4_t *b,
                                                             graphene_vec4_t       *res);
    float                   graphene_vec4_get_x             (const graphene_vec4_t *v);
    float                   graphene_vec4_get_y             (const graphene_vec4_t *v);
    float                   graphene_vec4_get_z             (const graphene_vec4_t *v);
    float                   graphene_vec4_get_w             (const graphene_vec4_t *v);
    void                    graphene_vec4_get_xy            (const graphene_vec4_t *v,
                                                             graphene_vec2_t       *res);
    void                    graphene_vec4_get_xyz           (const graphene_vec4_t *v,
                                                             graphene_vec3_t       *res);
    const graphene_vec4_t * graphene_vec4_zero              (void);
    const graphene_vec4_t * graphene_vec4_one               (void);
    const graphene_vec4_t * graphene_vec4_x_axis            (void);
    const graphene_vec4_t * graphene_vec4_y_axis            (void);
    const graphene_vec4_t * graphene_vec4_z_axis            (void);
    const graphene_vec4_t * graphene_vec4_w_axis            (void);
    
    // graphene-matrix.h
    graphene_matrix_t *     graphene_matrix_alloc                   (void);
    void                    graphene_matrix_free                    (graphene_matrix_t        *m);
    graphene_matrix_t *     graphene_matrix_init_identity           (graphene_matrix_t        *m);
    graphene_matrix_t *     graphene_matrix_init_from_float         (graphene_matrix_t        *m,
                                                                     const float              *v);
    graphene_matrix_t *     graphene_matrix_init_from_vec4          (graphene_matrix_t        *m,
                                                                     const graphene_vec4_t    *v0,
                                                                     const graphene_vec4_t    *v1,
                                                                     const graphene_vec4_t    *v2,
                                                                     const graphene_vec4_t    *v3);
    graphene_matrix_t *     graphene_matrix_init_from_matrix        (graphene_matrix_t        *m,
                                                                     const graphene_matrix_t  *src);
    graphene_matrix_t *     graphene_matrix_init_perspective        (graphene_matrix_t        *m,
                                                                     float                     fovy,
                                                                     float                     aspect,
                                                                     float                     z_near,
                                                                     float                     z_far);
    graphene_matrix_t *     graphene_matrix_init_ortho              (graphene_matrix_t        *m,
                                                                     float                     left,
                                                                     float                     right,
                                                                     float                     top,
                                                                     float                     bottom,
                                                                     float                     z_near,
                                                                     float                     z_far);
    graphene_matrix_t *     graphene_matrix_init_look_at            (graphene_matrix_t        *m,
                                                                     const graphene_vec3_t    *eye,
                                                                     const graphene_vec3_t    *center,
                                                                     const graphene_vec3_t    *up);
    graphene_matrix_t *     graphene_matrix_init_frustum            (graphene_matrix_t        *m,
                                                                     float                     left,
                                                                     float                     right,
                                                                     float                     bottom,
                                                                     float                     top,
                                                                     float                     z_near,
                                                                     float                     z_far);
    graphene_matrix_t *     graphene_matrix_init_scale              (graphene_matrix_t        *m,
                                                                     float                     x,
                                                                     float                     y,
                                                                     float                     z);
    graphene_matrix_t *     graphene_matrix_init_translate          (graphene_matrix_t        *m,
                                                                     const graphene_point3d_t *p);
    graphene_matrix_t *     graphene_matrix_init_rotate             (graphene_matrix_t        *m,
                                                                     float                     angle,
                                                                     const graphene_vec3_t    *axis);
    graphene_matrix_t *     graphene_matrix_init_skew               (graphene_matrix_t        *m,
                                                                     float                     x_skew,
                                                                     float                     y_skew);
    graphene_matrix_t *     graphene_matrix_init_from_2d            (graphene_matrix_t        *m,
                                                                     double                    xx,
                                                                     double                    yx,
                                                                     double                    xy,
                                                                     double                    yy,
                                                                     double                    x_0,
                                                                     double                    y_0);
    bool                    graphene_matrix_is_identity             (const graphene_matrix_t  *m);
    bool                    graphene_matrix_is_2d                   (const graphene_matrix_t  *m);
    bool                    graphene_matrix_is_backface_visible     (const graphene_matrix_t  *m);
    bool                    graphene_matrix_is_singular             (const graphene_matrix_t  *m);
    void                    graphene_matrix_to_float                (const graphene_matrix_t  *m,
                                                                     float                    *v);
    bool                    graphene_matrix_to_2d                   (const graphene_matrix_t  *m,
                                                                     double                   *xx,
                                                                     double                   *yx,
                                                                     double                   *xy,
                                                                     double                   *yy,
                                                                     double                   *x_0,
                                                                     double                   *y_0);
    void                    graphene_matrix_get_row                 (const graphene_matrix_t  *m,
                                                                     unsigned int              index_,
                                                                     graphene_vec4_t          *res);
    float                   graphene_matrix_get_value               (const graphene_matrix_t  *m,
                                                                     unsigned int              row,
                                                                     unsigned int              col);
    void                    graphene_matrix_multiply                (const graphene_matrix_t  *a,
                                                                     const graphene_matrix_t  *b,
                                                                     graphene_matrix_t        *res);
    float                   graphene_matrix_determinant             (const graphene_matrix_t  *m);
    void                    graphene_matrix_transform_vec4          (const graphene_matrix_t  *m,
                                                                     const graphene_vec4_t    *v,
                                                                     graphene_vec4_t          *res);
    void                    graphene_matrix_transform_vec3          (const graphene_matrix_t  *m,
                                                                     const graphene_vec3_t    *v,
                                                                     graphene_vec3_t          *res);
    void                    graphene_matrix_transform_point         (const graphene_matrix_t  *m,
                                                                     const graphene_point_t   *p,
                                                                     graphene_point_t         *res);
    void                    graphene_matrix_transform_point3d       (const graphene_matrix_t  *m,
                                                                     const graphene_point3d_t *p,
                                                                     graphene_point3d_t       *res);
    void                    graphene_matrix_transform_rect          (const graphene_matrix_t  *m,
                                                                     const graphene_rect_t    *r,
                                                                     graphene_quad_t          *res);
    void                    graphene_matrix_transform_bounds        (const graphene_matrix_t  *m,
                                                                     const graphene_rect_t    *r,
                                                                     graphene_rect_t          *res);
    void                    graphene_matrix_transform_sphere        (const graphene_matrix_t  *m,
                                                                     const graphene_sphere_t  *s,
                                                                     graphene_sphere_t        *res);
    void                    graphene_matrix_transform_box           (const graphene_matrix_t  *m,
                                                                     const graphene_box_t     *b,
                                                                     graphene_box_t           *res);
    void                    graphene_matrix_transform_ray           (const graphene_matrix_t  *m,
                                                                     const graphene_ray_t     *r,
                                                                     graphene_ray_t           *res);
    void                    graphene_matrix_project_point           (const graphene_matrix_t  *m,
                                                                     const graphene_point_t   *p,
                                                                     graphene_point_t         *res);
    void                    graphene_matrix_project_rect_bounds     (const graphene_matrix_t  *m,
                                                                     const graphene_rect_t    *r,
                                                                     graphene_rect_t          *res);
    void                    graphene_matrix_project_rect            (const graphene_matrix_t  *m,
                                                                     const graphene_rect_t    *r,
                                                                     graphene_quad_t          *res);
    bool                    graphene_matrix_untransform_point       (const graphene_matrix_t  *m,
                                                                     const graphene_point_t   *p,
                                                                     const graphene_rect_t    *bounds,
                                                                     graphene_point_t         *res);
    void                    graphene_matrix_untransform_bounds      (const graphene_matrix_t  *m,
                                                                     const graphene_rect_t    *r,
                                                                     const graphene_rect_t    *bounds,
                                                                     graphene_rect_t          *res);
    void                    graphene_matrix_unproject_point3d       (const graphene_matrix_t  *projection,
                                                                     const graphene_matrix_t  *modelview,
                                                                     const graphene_point3d_t *point,
                                                                     graphene_point3d_t       *res);
    void                    graphene_matrix_translate               (graphene_matrix_t        *m,
                                                                     const graphene_point3d_t *pos);
    void                    graphene_matrix_rotate                  (graphene_matrix_t        *m,
                                                                     float                     angle,
                                                                     const graphene_vec3_t    *axis);
    void                    graphene_matrix_rotate_x                (graphene_matrix_t        *m,
                                                                     float                     angle);
    void                    graphene_matrix_rotate_y                (graphene_matrix_t        *m,
                                                                     float                     angle);
    void                    graphene_matrix_rotate_z                (graphene_matrix_t        *m,
                                                                     float                     angle);
    void                    graphene_matrix_rotate_quaternion       (graphene_matrix_t        *m,
                                                                     const graphene_quaternion_t *q);
    void                    graphene_matrix_rotate_euler            (graphene_matrix_t        *m,
                                                                     const graphene_euler_t   *e);
    void                    graphene_matrix_scale                   (graphene_matrix_t        *m,
                                                                     float                     factor_x,
                                                                     float                     factor_y,
                                                                     float                     factor_z);
    void                    graphene_matrix_skew_xy                 (graphene_matrix_t        *m,
                                                                     float                     factor);
    void                    graphene_matrix_skew_xz                 (graphene_matrix_t        *m,
                                                                     float                     factor);
    void                    graphene_matrix_skew_yz                 (graphene_matrix_t        *m,
                                                                     float                     factor);
    void                    graphene_matrix_transpose               (const graphene_matrix_t  *m,
                                                                     graphene_matrix_t        *res);
    void                    graphene_matrix_inverse                 (const graphene_matrix_t  *m,
                                                                     graphene_matrix_t        *res);
    void                    graphene_matrix_perspective             (const graphene_matrix_t  *m,
                                                                     float                     depth,
                                                                     graphene_matrix_t        *res);
    void                    graphene_matrix_normalize               (const graphene_matrix_t  *m,
                                                                     graphene_matrix_t        *res);
    float                   graphene_matrix_get_x_scale             (const graphene_matrix_t  *m);
    float                   graphene_matrix_get_y_scale             (const graphene_matrix_t  *m);
    float                   graphene_matrix_get_z_scale             (const graphene_matrix_t  *m);
    void                    graphene_matrix_interpolate             (const graphene_matrix_t  *a,
                                                                     const graphene_matrix_t  *b,
                                                                     double                    factor,
                                                                     graphene_matrix_t        *res);
    void                    graphene_matrix_print                   (const graphene_matrix_t  *m);

    // graphene-point.h
    graphene_point_t *              graphene_point_alloc            (void);
    void                            graphene_point_free             (graphene_point_t       *p);
    graphene_point_t *              graphene_point_init             (graphene_point_t       *p,
                                                                     float                   x,
                                                                     float                   y);
    graphene_point_t *              graphene_point_init_from_point  (graphene_point_t       *p,
                                                                     const graphene_point_t *src);
    graphene_point_t *              graphene_point_init_from_vec2   (graphene_point_t       *p,
                                                                     const graphene_vec2_t  *src);
    bool                            graphene_point_equal            (const graphene_point_t *a,
                                                                     const graphene_point_t *b);
    float                           graphene_point_distance         (const graphene_point_t *a,
                                                                     const graphene_point_t *b,
                                                                     float                  *d_x,
                                                                     float                  *d_y);
    bool                            graphene_point_near             (const graphene_point_t *a,
                                                                     const graphene_point_t *b,
                                                                     float                   epsilon);
    void                            graphene_point_interpolate      (const graphene_point_t *a,
                                                                     const graphene_point_t *b,
                                                                     double                  factor,
                                                                     graphene_point_t       *res);
    void                            graphene_point_to_vec2          (const graphene_point_t *p,
                                                                     graphene_vec2_t        *v);
    const graphene_point_t *        graphene_point_zero             (void);
    // graphene-size.h
    graphene_size_t *               graphene_size_alloc             (void);
    void                            graphene_size_free              (graphene_size_t        *s);
    graphene_size_t *               graphene_size_init              (graphene_size_t        *s,
                                                                     float                   width,
                                                                     float                   height);
    graphene_size_t *               graphene_size_init_from_size    (graphene_size_t        *s,
                                                                     const graphene_size_t  *src);
    bool                            graphene_size_equal             (const graphene_size_t  *a,
                                                                     const graphene_size_t  *b);
    void                            graphene_size_scale             (const graphene_size_t  *s,
                                                                     float                   factor,
                                                                     graphene_size_t        *res);
    void                            graphene_size_interpolate       (const graphene_size_t  *a,
                                                                     const graphene_size_t  *b,
                                                                     double                  factor,
                                                                     graphene_size_t        *res);
    const graphene_size_t *         graphene_size_zero              (void);
    
    // graphene-rect.h
    graphene_rect_t *       graphene_rect_alloc             (void);
    void                    graphene_rect_free              (graphene_rect_t       *r);
    graphene_rect_t *       graphene_rect_init              (graphene_rect_t       *r,
                                                             float                  x,
                                                             float                  y,
                                                             float                  width,
                                                             float                  height);
    graphene_rect_t *       graphene_rect_init_from_rect    (graphene_rect_t       *r,
                                                             const graphene_rect_t *src);
    bool                    graphene_rect_equal             (const graphene_rect_t *a,
                                                             const graphene_rect_t *b);
    graphene_rect_t *       graphene_rect_normalize         (graphene_rect_t       *r);
    void                    graphene_rect_normalize_r       (const graphene_rect_t *r,
                                                             graphene_rect_t       *res);
    void                    graphene_rect_get_center        (const graphene_rect_t *r,
                                                             graphene_point_t      *p);
    void                    graphene_rect_get_top_left      (const graphene_rect_t *r,
                                                             graphene_point_t      *p);
    void                    graphene_rect_get_top_right     (const graphene_rect_t *r,
                                                             graphene_point_t      *p);
    void                    graphene_rect_get_bottom_right  (const graphene_rect_t *r,
                                                             graphene_point_t      *p);
    void                    graphene_rect_get_bottom_left   (const graphene_rect_t *r,
                                                             graphene_point_t      *p);
    void                    graphene_rect_get_vertices      (const graphene_rect_t *r,
                                                             graphene_vec2_t        vertices[]);
    float                   graphene_rect_get_x             (const graphene_rect_t *r);
    float                   graphene_rect_get_y             (const graphene_rect_t *r);
    float                   graphene_rect_get_width         (const graphene_rect_t *r);
    float                   graphene_rect_get_height        (const graphene_rect_t *r);
    void                    graphene_rect_union             (const graphene_rect_t *a,
                                                             const graphene_rect_t *b,
                                                             graphene_rect_t       *res);
    bool                    graphene_rect_intersection      (const graphene_rect_t *a,
                                                             const graphene_rect_t *b,
                                                             graphene_rect_t       *res);
    bool                    graphene_rect_contains_point    (const graphene_rect_t  *r,
                                                             const graphene_point_t *p);
    bool                    graphene_rect_contains_rect     (const graphene_rect_t  *a,
                                                             const graphene_rect_t  *b);
    graphene_rect_t *       graphene_rect_offset            (graphene_rect_t        *r,
                                                             float                   d_x,
                                                             float                   d_y);
    void                    graphene_rect_offset_r          (const graphene_rect_t  *r,
                                                             float                   d_x,
                                                             float                   d_y,
                                                             graphene_rect_t        *res);
    graphene_rect_t *       graphene_rect_inset             (graphene_rect_t        *r,
                                                             float                   d_x,
                                                             float                   d_y);
    void                    graphene_rect_inset_r           (const graphene_rect_t  *r,
                                                             float                   d_x,
                                                             float                   d_y,
                                                             graphene_rect_t        *res);
    // (graphene_rect_round)
    graphene_rect_t *       graphene_rect_round_to_pixel    (graphene_rect_t        *r);
    void                    graphene_rect_round             (const graphene_rect_t  *r,
                                                             graphene_rect_t        *res);
    void                    graphene_rect_interpolate       (const graphene_rect_t  *a,
                                                             const graphene_rect_t  *b,
                                                             double                  factor,
                                                             graphene_rect_t        *res);
    void                    graphene_rect_expand            (const graphene_rect_t  *r,
                                                             const graphene_point_t *p,
                                                             graphene_rect_t        *res);
    
    // graphene-point3d.h
    graphene_point3d_t *            graphene_point3d_alloc                  (void);
    void                            graphene_point3d_free                   (graphene_point3d_t       *p);
    graphene_point3d_t *            graphene_point3d_init                   (graphene_point3d_t       *p,
                                                                             float                     x,
                                                                             float                     y,
                                                                             float                     z);
    graphene_point3d_t *            graphene_point3d_init_from_point        (graphene_point3d_t       *p,
                                                                             const graphene_point3d_t *src);
    graphene_point3d_t *            graphene_point3d_init_from_vec3         (graphene_point3d_t       *p,
                                                                             const graphene_vec3_t    *v);
    void                            graphene_point3d_to_vec3                (const graphene_point3d_t *p,
                                                                             graphene_vec3_t          *v);
    bool                            graphene_point3d_equal                  (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b);
    bool                            graphene_point3d_near                   (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b,
                                                                             float                     epsilon);
    void                            graphene_point3d_scale                  (const graphene_point3d_t *p,
                                                                             float                     factor,
                                                                             graphene_point3d_t       *res);
    void                            graphene_point3d_cross                  (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b,
                                                                             graphene_point3d_t       *res);
    float                           graphene_point3d_dot                    (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b);
    float                           graphene_point3d_length                 (const graphene_point3d_t *p);
    void                            graphene_point3d_normalize              (const graphene_point3d_t *p,
                                                                             graphene_point3d_t       *res);
    float                           graphene_point3d_distance               (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b,
                                                                             graphene_vec3_t          *delta);
    void                            graphene_point3d_interpolate            (const graphene_point3d_t *a,
                                                                             const graphene_point3d_t *b,
                                                                             double                    factor,
                                                                             graphene_point3d_t       *res);
    void                            graphene_point3d_normalize_viewport     (const graphene_point3d_t *p,
                                                                             const graphene_rect_t    *viewport,
                                                                             float                     z_near,
                                                                             float                     z_far,
                                                                             graphene_point3d_t       *res);
    const graphene_point3d_t *      graphene_point3d_zero                   (void);
    
    // graphene-quad.h
    graphene_quad_t *       graphene_quad_alloc             (void);
    void                    graphene_quad_free              (graphene_quad_t        *q);
    graphene_quad_t *       graphene_quad_init              (graphene_quad_t        *q,
                                                             const graphene_point_t *p1,
                                                             const graphene_point_t *p2,
                                                             const graphene_point_t *p3,
                                                             const graphene_point_t *p4);
    graphene_quad_t *       graphene_quad_init_from_rect    (graphene_quad_t        *q,
                                                             const graphene_rect_t  *r);
    graphene_quad_t *       graphene_quad_init_from_points  (graphene_quad_t        *q,
                                                             const graphene_point_t  points[]);
    bool                    graphene_quad_contains          (const graphene_quad_t  *q,
                                                             const graphene_point_t *p);
    void                    graphene_quad_bounds            (const graphene_quad_t  *q,
                                                             graphene_rect_t        *r);
    const graphene_point_t *graphene_quad_get_point         (const graphene_quad_t  *q,
                                                             unsigned int            index_);
    
    // graphene-quaternion.h
    graphene_quaternion_t * graphene_quaternion_alloc                       (void);
    void                    graphene_quaternion_free                        (graphene_quaternion_t       *q);
    graphene_quaternion_t * graphene_quaternion_init                        (graphene_quaternion_t       *q,
                                                                             float                        x,
                                                                             float                        y,
                                                                             float                        z,
                                                                             float                        w);
    graphene_quaternion_t * graphene_quaternion_init_identity               (graphene_quaternion_t       *q);
    graphene_quaternion_t * graphene_quaternion_init_from_quaternion        (graphene_quaternion_t       *q,
                                                                             const graphene_quaternion_t *src);
    graphene_quaternion_t * graphene_quaternion_init_from_vec4              (graphene_quaternion_t       *q,
                                                                             const graphene_vec4_t       *src);
    graphene_quaternion_t * graphene_quaternion_init_from_matrix            (graphene_quaternion_t       *q,
                                                                             const graphene_matrix_t     *m);
    graphene_quaternion_t * graphene_quaternion_init_from_angles            (graphene_quaternion_t       *q,
                                                                             float                        deg_x,
                                                                             float                        deg_y,
                                                                             float                        deg_z);
    graphene_quaternion_t * graphene_quaternion_init_from_angle_vec3        (graphene_quaternion_t       *q,
                                                                             float                        angle,
                                                                             const graphene_vec3_t       *axis);
    graphene_quaternion_t * graphene_quaternion_init_from_euler             (graphene_quaternion_t       *q,
                                                                             const graphene_euler_t      *e);
    void                    graphene_quaternion_to_vec4                     (const graphene_quaternion_t *q,
                                                                             graphene_vec4_t             *res);
    void                    graphene_quaternion_to_matrix                   (const graphene_quaternion_t *q,
                                                                             graphene_matrix_t           *m);
    void                    graphene_quaternion_to_angles                   (const graphene_quaternion_t *q,
                                                                             float                       *deg_x,
                                                                             float                       *deg_y,
                                                                             float                       *deg_z);
    void                    graphene_quaternion_to_angle_vec3               (const graphene_quaternion_t *q,
                                                                             float                       *angle,
                                                                             graphene_vec3_t             *axis);
    bool                    graphene_quaternion_equal                       (const graphene_quaternion_t *a,
                                                                             const graphene_quaternion_t *b);
    float                   graphene_quaternion_dot                         (const graphene_quaternion_t *a,
                                                                             const graphene_quaternion_t *b);
    void                    graphene_quaternion_invert                      (const graphene_quaternion_t *q,
                                                                             graphene_quaternion_t       *res);
    void                    graphene_quaternion_normalize                   (const graphene_quaternion_t *q,
                                                                             graphene_quaternion_t       *res);
    void                    graphene_quaternion_slerp                       (const graphene_quaternion_t *a,
                                                                             const graphene_quaternion_t *b,
                                                                             float                        factor,
                                                                             graphene_quaternion_t       *res);
    
    // graphene-euler.h
    graphene_euler_t *      graphene_euler_alloc                    (void);
    void                    graphene_euler_free                     (graphene_euler_t            *e);
    graphene_euler_t *      graphene_euler_init                     (graphene_euler_t            *e,
                                                                     float                        x,
                                                                     float                        y,
                                                                     float                        z);
    graphene_euler_t *      graphene_euler_init_with_order          (graphene_euler_t            *e,
                                                                     float                        x,
                                                                     float                        y,
                                                                     float                        z,
                                                                     graphene_euler_order_t       order);
    graphene_euler_t *      graphene_euler_init_from_matrix         (graphene_euler_t            *e,
                                                                     const graphene_matrix_t     *m,
                                                                     graphene_euler_order_t       order);
    graphene_euler_t *      graphene_euler_init_from_quaternion     (graphene_euler_t            *e,
                                                                     const graphene_quaternion_t *q,
                                                                     graphene_euler_order_t       order);
    graphene_euler_t *      graphene_euler_init_from_vec3           (graphene_euler_t            *e,
                                                                     const graphene_vec3_t       *v,
                                                                     graphene_euler_order_t       order);
    graphene_euler_t *      graphene_euler_init_from_euler          (graphene_euler_t            *e,
                                                                     const graphene_euler_t      *src);
    bool                    graphene_euler_equal                    (const graphene_euler_t      *a,
                                                                     const graphene_euler_t      *b);
    float                   graphene_euler_get_x                    (const graphene_euler_t      *e);
    float                   graphene_euler_get_y                    (const graphene_euler_t      *e);
    float                   graphene_euler_get_z                    (const graphene_euler_t      *e);
    graphene_euler_order_t  graphene_euler_get_order                (const graphene_euler_t      *e);
    void                    graphene_euler_to_vec3                  (const graphene_euler_t      *e,
                                                                     graphene_vec3_t             *res);
    void                    graphene_euler_to_matrix                (const graphene_euler_t      *e,
                                                                     graphene_matrix_t           *res);
    void                    graphene_euler_reorder                  (const graphene_euler_t      *e,
                                                                     graphene_euler_order_t       order,
                                                                     graphene_euler_t            *res);
    
    // graphene-plane.h
    graphene_plane_t *              graphene_plane_alloc            (void);
    void                            graphene_plane_free             (graphene_plane_t         *p);
    graphene_plane_t *              graphene_plane_init             (graphene_plane_t         *p,
                                                                     const graphene_vec3_t    *normal,
                                                                     float                     constant);
    graphene_plane_t *              graphene_plane_init_from_vec4   (graphene_plane_t         *p,
                                                                     const graphene_vec4_t    *src);
    graphene_plane_t *              graphene_plane_init_from_plane  (graphene_plane_t         *p,
                                                                     const graphene_plane_t   *src);
    graphene_plane_t *              graphene_plane_init_from_point  (graphene_plane_t         *p,
                                                                     const graphene_vec3_t    *normal,
                                                                     const graphene_point3d_t *point);
    graphene_plane_t *              graphene_plane_init_from_points (graphene_plane_t         *p,
                                                                     const graphene_point3d_t *a,
                                                                     const graphene_point3d_t *b,
                                                                     const graphene_point3d_t *c);
    void                            graphene_plane_normalize        (const graphene_plane_t   *p,
                                                                     graphene_plane_t         *res);
    void                            graphene_plane_negate           (const graphene_plane_t   *p,
                                                                     graphene_plane_t         *res);
    bool                            graphene_plane_equal            (const graphene_plane_t   *p1,
                                                                     const graphene_plane_t   *p2);
    float                           graphene_plane_distance         (const graphene_plane_t   *p,
                                                                     const graphene_point3d_t *point);
    void                            graphene_plane_get_normal       (const graphene_plane_t   *p,
                                                                     graphene_vec3_t          *normal);
    float                           graphene_plane_get_constant     (const graphene_plane_t   *p);
    
    // graphene-frustum.h
    graphene_frustum_t *    graphene_frustum_alloc                  (void);
    void                    graphene_frustum_free                   (graphene_frustum_t *f);
    graphene_frustum_t *    graphene_frustum_init                   (graphene_frustum_t       *f,
                                                                     const graphene_plane_t   *p0,
                                                                     const graphene_plane_t   *p1,
                                                                     const graphene_plane_t   *p2,
                                                                     const graphene_plane_t   *p3,
                                                                     const graphene_plane_t   *p4,
                                                                     const graphene_plane_t   *p5);
    graphene_frustum_t *    graphene_frustum_init_from_frustum      (graphene_frustum_t       *f,
                                                                     const graphene_frustum_t *src);
    graphene_frustum_t *    graphene_frustum_init_from_matrix       (graphene_frustum_t       *f,
                                                                     const graphene_matrix_t  *matrix);
    bool                    graphene_frustum_contains_point         (const graphene_frustum_t *f,
                                                                     const graphene_point3d_t *point);
    bool                    graphene_frustum_intersects_sphere      (const graphene_frustum_t *f,
                                                                     const graphene_sphere_t  *sphere);
    bool                    graphene_frustum_intersects_box         (const graphene_frustum_t *f,
                                                                     const graphene_box_t     *box);
    void                    graphene_frustum_get_planes             (const graphene_frustum_t *f,
                                                                     graphene_plane_t          planes[]);
    
    // graphene-sphere.h
    graphene_sphere_t *     graphene_sphere_alloc                   (void);
    void                    graphene_sphere_free                    (graphene_sphere_t        *s);
    graphene_sphere_t *     graphene_sphere_init                    (graphene_sphere_t        *s,
                                                                     const graphene_point3d_t *center,
                                                                     float                     radius);
    graphene_sphere_t *     graphene_sphere_init_from_points        (graphene_sphere_t        *s,
                                                                     unsigned int              n_points,
                                                                     const graphene_point3d_t *points,
                                                                     const graphene_point3d_t *center);
    graphene_sphere_t *     graphene_sphere_init_from_vectors       (graphene_sphere_t        *s,
                                                                     unsigned int              n_vectors,
                                                                     const graphene_vec3_t    *vectors,
                                                                     const graphene_point3d_t *center);
    void                    graphene_sphere_get_center              (const graphene_sphere_t  *s,
                                                                     graphene_point3d_t       *center);
    float                   graphene_sphere_get_radius              (const graphene_sphere_t  *s);
    bool                    graphene_sphere_is_empty                (const graphene_sphere_t  *s);
    bool                    graphene_sphere_equal                   (const graphene_sphere_t  *a,
                                                                     const graphene_sphere_t  *b);
    bool                    graphene_sphere_contains_point          (const graphene_sphere_t  *s,
                                                                     const graphene_point3d_t *point);
    float                   graphene_sphere_distance                (const graphene_sphere_t  *s,
                                                                     const graphene_point3d_t *point);
    void                    graphene_sphere_get_bounding_box        (const graphene_sphere_t  *s,
                                                                     graphene_box_t           *box);
    void                    graphene_sphere_translate               (const graphene_sphere_t  *s,
                                                                     const graphene_point3d_t *point,
                                                                     graphene_sphere_t        *res);
    
    // graphene-box.h
    graphene_box_t *        graphene_box_alloc                      (void);
    void                    graphene_box_free                       (graphene_box_t           *box);
    graphene_box_t *        graphene_box_init                       (graphene_box_t           *box,
                                                                     const graphene_point3d_t *min,
                                                                     const graphene_point3d_t *max);
    graphene_box_t *        graphene_box_init_from_points           (graphene_box_t           *box,
                                                                     unsigned int              n_points,
                                                                     const graphene_point3d_t *points);
    graphene_box_t *        graphene_box_init_from_vectors          (graphene_box_t           *box,
                                                                     unsigned int              n_vectors,
                                                                     const graphene_vec3_t    *vectors);
    graphene_box_t *        graphene_box_init_from_box              (graphene_box_t           *box,
                                                                     const graphene_box_t     *src);
    graphene_box_t *        graphene_box_init_from_vec3             (graphene_box_t           *box,
                                                                     const graphene_vec3_t    *min,
                                                                     const graphene_vec3_t    *max);
    void                    graphene_box_expand                     (const graphene_box_t     *box,
                                                                     const graphene_point3d_t *point,
                                                                     graphene_box_t           *res);
    void                    graphene_box_expand_vec3                (const graphene_box_t     *box,
                                                                     const graphene_vec3_t    *vec,
                                                                     graphene_box_t           *res);
    void                    graphene_box_expand_scalar              (const graphene_box_t     *box,
                                                                     float                     scalar,
                                                                     graphene_box_t           *res);
    void                    graphene_box_union                      (const graphene_box_t     *a,
                                                                     const graphene_box_t     *b,
                                                                     graphene_box_t           *res);
    bool                    graphene_box_intersection               (const graphene_box_t     *a,
                                                                     const graphene_box_t     *b,
                                                                     graphene_box_t           *res);
    float                   graphene_box_get_width                  (const graphene_box_t     *box);
    float                   graphene_box_get_height                 (const graphene_box_t     *box);
    float                   graphene_box_get_depth                  (const graphene_box_t     *box);
    void                    graphene_box_get_size                   (const graphene_box_t     *box,
                                                                     graphene_vec3_t          *size);
    void                    graphene_box_get_center                 (const graphene_box_t     *box,
                                                                     graphene_point3d_t       *center);
    void                    graphene_box_get_min                    (const graphene_box_t     *box,
                                                                     graphene_point3d_t       *min);
    void                    graphene_box_get_max                    (const graphene_box_t     *box,
                                                                     graphene_point3d_t       *max);
    void                    graphene_box_get_vertices               (const graphene_box_t     *box,
                                                                     graphene_vec3_t           vertices[]);
    void                    graphene_box_get_bounding_sphere        (const graphene_box_t     *box,
                                                                     graphene_sphere_t        *sphere);
    bool                    graphene_box_contains_point             (const graphene_box_t     *box,
                                                                     const graphene_point3d_t *point);
    bool                    graphene_box_contains_box               (const graphene_box_t     *a,
                                                                     const graphene_box_t     *b);
    bool                    graphene_box_equal                      (const graphene_box_t     *a,
                                                                     const graphene_box_t     *b);
    const graphene_box_t *  graphene_box_zero                       (void);
    const graphene_box_t *  graphene_box_one                        (void);
    const graphene_box_t *  graphene_box_minus_one                  (void);
    const graphene_box_t *  graphene_box_one_minus_one              (void);
    const graphene_box_t *  graphene_box_infinite                   (void);
    const graphene_box_t *  graphene_box_empty                      (void);
    
    // graphene-triangle.h
    graphene_triangle_t *   graphene_triangle_alloc                 (void);
    void                    graphene_triangle_free                  (graphene_triangle_t *t);
    graphene_triangle_t *   graphene_triangle_init_from_point3d     (graphene_triangle_t       *t,
                                                                     const graphene_point3d_t  *a,
                                                                     const graphene_point3d_t  *b,
                                                                     const graphene_point3d_t  *c);
    graphene_triangle_t *   graphene_triangle_init_from_vec3        (graphene_triangle_t       *t,
                                                                     const graphene_vec3_t     *a,
                                                                     const graphene_vec3_t     *b,
                                                                     const graphene_vec3_t     *c);
    void                    graphene_triangle_get_points            (const graphene_triangle_t *t,
                                                                     graphene_point3d_t        *a,
                                                                     graphene_point3d_t        *b,
                                                                     graphene_point3d_t        *c);
    void                    graphene_triangle_get_vertices          (const graphene_triangle_t *t,
                                                                     graphene_vec3_t           *a,
                                                                     graphene_vec3_t           *b,
                                                                     graphene_vec3_t           *c);
    float                   graphene_triangle_get_area              (const graphene_triangle_t *t);
    void                    graphene_triangle_get_midpoint          (const graphene_triangle_t *t,
                                                                     graphene_point3d_t        *res);
    void                    graphene_triangle_get_normal            (const graphene_triangle_t *t,
                                                                     graphene_vec3_t           *res);
    void                    graphene_triangle_get_plane             (const graphene_triangle_t *t,
                                                                     graphene_plane_t          *res);
    void                    graphene_triangle_get_bounding_box      (const graphene_triangle_t *t,
                                                                     graphene_box_t            *res);
    bool                    graphene_triangle_get_barycoords        (const graphene_triangle_t *t,
                                                                     const graphene_point3d_t  *p,
                                                                     graphene_vec2_t           *res);
    bool                    graphene_triangle_contains_point        (const graphene_triangle_t *t,
                                                                     const graphene_point3d_t  *p);
    bool                    graphene_triangle_equal                 (const graphene_triangle_t *a,
                                                                     const graphene_triangle_t *b);
    
    // graphene-ray.h
    graphene_ray_t *                graphene_ray_alloc                  (void);
    void                            graphene_ray_free                   (graphene_ray_t           *r);
    graphene_ray_t *                graphene_ray_init                   (graphene_ray_t           *r,
                                                                         const graphene_point3d_t *origin,
                                                                         const graphene_vec3_t    *direction);
    graphene_ray_t *                graphene_ray_init_from_ray          (graphene_ray_t           *r,
                                                                         const graphene_ray_t     *src);
    graphene_ray_t *                graphene_ray_init_from_vec3         (graphene_ray_t           *r,
                                                                         const graphene_vec3_t    *origin,
                                                                         const graphene_vec3_t    *direction);
    void                            graphene_ray_get_origin             (const graphene_ray_t     *r,
                                                                         graphene_point3d_t       *origin);
    void                            graphene_ray_get_direction          (const graphene_ray_t     *r,
                                                                         graphene_vec3_t          *direction);
    void                            graphene_ray_get_position_at        (const graphene_ray_t     *r,
                                                                         float                     t,
                                                                         graphene_point3d_t       *position);
    float                           graphene_ray_get_distance_to_point  (const graphene_ray_t     *r,
                                                                         const graphene_point3d_t *p);
    float                           graphene_ray_get_distance_to_plane  (const graphene_ray_t     *r,
                                                                         const graphene_plane_t   *p);
    bool                            graphene_ray_equal                  (const graphene_ray_t     *a,
                                                                         const graphene_ray_t     *b);
    void                            graphene_ray_get_closest_point_to_point   (const graphene_ray_t     *r,
                                                                               const graphene_point3d_t *p,
                                                                               graphene_point3d_t       *res);
''')

ffi.compile()
